/*
 * Checks visible MDX docs pages for links to hidden docs pages.
 *
 * A target page is considered hidden when it has `hidden: true` in its MDX
 * frontmatter, or when it appears as a `hidden: true` nav entry under the
 * `# HIDDEN SECTION` marker in `fern/v1.yml` or `fern/v2.yml`.
 *
 * The checker writes the full report to:
 *   doc-workflows/reports/hidden-links.md
 *
 * Run locally with:
 *   node .github/scripts/check-hidden-links.cjs
 */
const fs = require("fs").promises;
const path = require("path");
const matter = require("gray-matter");

const repoRoot = path.join(__dirname, "../..");
const fernDir = path.join(repoRoot, "fern");
const pagesDir = path.join(fernDir, "pages");
const reportPath = path.join(repoRoot, "doc-workflows/reports/hidden-links.md");
const navFiles = [
  { version: "v1", filePath: path.join(fernDir, "v1.yml") },
  { version: "v2", filePath: path.join(fernDir, "v2.yml") },
];

function toPosix(filePath) {
  return filePath.split(path.sep).join("/");
}

function repoRelative(filePath) {
  return toPosix(path.relative(repoRoot, filePath));
}

function normalizePagePath(pagePath) {
  return toPosix(pagePath).replace(/^fern\//, "");
}

async function walkMdxFiles(dirPath) {
  const entries = await fs.readdir(dirPath, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    const fullPath = path.join(dirPath, entry.name);

    if (entry.isDirectory()) {
      files.push(...(await walkMdxFiles(fullPath)));
      continue;
    }

    if (entry.isFile() && entry.name.endsWith(".mdx")) {
      files.push(fullPath);
    }
  }

  return files;
}

async function buildPageIndex() {
  const files = await walkMdxFiles(pagesDir);
  const pages = new Map();

  for (const filePath of files) {
    const fileContent = await fs.readFile(filePath, "utf8");
    const parsed = parseMdxContent(fileContent, filePath);
    const pagePath = normalizePagePath(path.relative(fernDir, filePath));

    pages.set(pagePath, {
      filePath,
      repoPath: repoRelative(filePath),
      pagePath,
      content: parsed.content,
      frontmatter: parsed.data,
    });
  }

  return pages;
}

function parseMdxContent(fileContent, filePath) {
  try {
    return matter(fileContent);
  } catch (error) {
    console.warn(
      `[WARN] Could not fully parse frontmatter for ${repoRelative(filePath)}: ${error.reason || error.message}`
    );
    return parseSimpleFrontmatter(fileContent);
  }
}

function parseSimpleFrontmatter(fileContent) {
  const frontmatterMatch = fileContent.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  const data = {};

  if (!frontmatterMatch) {
    return {
      data,
      content: fileContent,
    };
  }

  const frontmatter = frontmatterMatch[1];
  const slugMatch = frontmatter.match(/^slug:\s*["']?([^"'\r\n]+)["']?\s*$/m);
  const hiddenMatch = frontmatter.match(/^hidden:\s*(true|false)\s*$/m);

  if (slugMatch) {
    data.slug = slugMatch[1].trim();
  }

  if (hiddenMatch) {
    data.hidden = hiddenMatch[1] === "true";
  }

  return {
    data,
    content: fileContent.slice(frontmatterMatch[0].length),
  };
}

async function collectNavData() {
  const navMembership = new Map();
  const navHidden = new Map();

  for (const navFile of navFiles) {
    const content = await fs.readFile(navFile.filePath, "utf8");
    const allPathPattern = /path:\s*["']?(pages\/[^"'\s#]+\.mdx)["']?/g;

    for (const match of content.matchAll(allPathPattern)) {
      addToMapSet(navMembership, normalizePagePath(match[1]), navFile.version);
    }

    for (const hiddenPath of collectHiddenSectionPaths(content)) {
      addToMapSet(
        navHidden,
        normalizePagePath(hiddenPath),
        `${path.basename(navFile.filePath)} # HIDDEN SECTION`
      );
    }
  }

  return { navMembership, navHidden };
}

function collectHiddenSectionPaths(content) {
  const lines = content.split(/\r?\n/);
  const markerIndex = lines.findIndex((line) => line.includes("# HIDDEN SECTION"));
  const hiddenPaths = new Set();

  if (markerIndex === -1) {
    return hiddenPaths;
  }

  let currentItem = null;

  function commitCurrentItem() {
    if (currentItem?.hasHiddenTrue && currentItem.path) {
      hiddenPaths.add(currentItem.path);
    }
  }

  for (let index = markerIndex + 1; index < lines.length; index++) {
    const line = lines[index];
    const itemMatch = line.match(/^(\s*)-\s+(?:page|section):/);

    if (itemMatch) {
      commitCurrentItem();
      currentItem = {
        indent: itemMatch[1].length,
        hasHiddenTrue: false,
        path: null,
      };
      continue;
    }

    if (!currentItem) {
      continue;
    }

    const indent = line.match(/^(\s*)/)?.[1].length ?? 0;
    if (indent <= currentItem.indent) {
      continue;
    }

    if (/^\s*hidden:\s*true\s*(?:#.*)?$/.test(line)) {
      currentItem.hasHiddenTrue = true;
      continue;
    }

    const pathMatch = line.match(/^\s*path:\s*["']?(pages\/[^"'\s#]+\.mdx)["']?/);
    if (pathMatch) {
      currentItem.path = pathMatch[1];
    }
  }

  commitCurrentItem();
  return hiddenPaths;
}

function addToMapSet(map, key, value) {
  if (!map.has(key)) {
    map.set(key, new Set());
  }

  map.get(key).add(value);
}

function buildHiddenPages(pages, navHidden) {
  const hiddenPages = new Map();

  for (const page of pages.values()) {
    if (page.frontmatter.hidden === true) {
      addHiddenReason(hiddenPages, page.pagePath, "frontmatter hidden: true");
    }
  }

  for (const [pagePath, reasons] of navHidden.entries()) {
    for (const reason of reasons) {
      addHiddenReason(hiddenPages, pagePath, reason);
    }
  }

  return hiddenPages;
}

function addHiddenReason(hiddenPages, pagePath, reason) {
  if (!hiddenPages.has(pagePath)) {
    hiddenPages.set(pagePath, new Set());
  }

  hiddenPages.get(pagePath).add(reason);
}

function buildHiddenUrlMap(hiddenPages, pages, navMembership) {
  const hiddenUrlMap = new Map();

  for (const [pagePath, reasons] of hiddenPages.entries()) {
    const page = pages.get(pagePath);
    if (!page) {
      continue;
    }

    const aliases = buildUrlAliases(page, navMembership.get(pagePath) ?? new Set());

    for (const alias of aliases) {
      if (!hiddenUrlMap.has(alias)) {
        hiddenUrlMap.set(alias, []);
      }

      hiddenUrlMap.get(alias).push({
        pagePath,
        repoPath: page.repoPath,
        reasons: [...reasons].sort(),
      });
    }
  }

  return hiddenUrlMap;
}

function buildUrlAliases(page, navVersions) {
  const aliases = new Set();
  const slug = cleanSlug(page.frontmatter.slug);
  const docsSlug = docsSlugFromSlug(slug) ?? basenameSlug(page.pagePath);

  addFrontmatterSlugAliases(aliases, slug);

  if (navVersions.has("v1")) {
    aliases.add(`/v1/docs/${docsSlug}`);
  }

  if (navVersions.has("v2")) {
    aliases.add(`/docs/${docsSlug}`);
    aliases.add(`/v2/docs/${docsSlug}`);
  }

  if (navVersions.size === 0 && page.pagePath.startsWith("pages/v2/")) {
    aliases.add(`/docs/${docsSlug}`);
    aliases.add(`/v2/docs/${docsSlug}`);
  }

  return [...aliases].map(normalizePathOnlyUrl).filter(Boolean);
}

function cleanSlug(slug) {
  if (typeof slug !== "string") {
    return null;
  }

  return slug.trim().replace(/^\/+/, "").replace(/[?#].*$/, "").replace(/\/+$/, "");
}

function addFrontmatterSlugAliases(aliases, slug) {
  if (!slug) {
    return;
  }

  if (slug.startsWith("v1/docs/")) {
    aliases.add(`/${slug}`);
    return;
  }

  if (slug.startsWith("v2/docs/")) {
    aliases.add(`/${slug}`);
    aliases.add(`/docs/${slug.slice("v2/docs/".length)}`);
    return;
  }

  if (slug.startsWith("docs/")) {
    aliases.add(`/${slug}`);
    aliases.add(`/v2/${slug}`);
    return;
  }

  aliases.add(`/${slug}`);
}

function docsSlugFromSlug(slug) {
  if (!slug) {
    return null;
  }

  for (const prefix of ["v1/docs/", "v2/docs/", "docs/"]) {
    if (slug.startsWith(prefix)) {
      return slug.slice(prefix.length);
    }
  }

  return null;
}

function basenameSlug(pagePath) {
  const parsedPath = path.posix.parse(pagePath);
  return parsedPath.name === "index"
    ? path.posix.basename(parsedPath.dir)
    : parsedPath.name;
}

function selectSourcePages(pages, hiddenPages) {
  return [...pages.values()].filter((page) => {
    if (hiddenPages.has(page.pagePath)) {
      return false;
    }

    if (page.pagePath.startsWith("pages/-ARCHIVE-/")) {
      return false;
    }

    if (page.pagePath.startsWith("pages/changelog/")) {
      return false;
    }

    return true;
  });
}

function findViolations(sourcePages, hiddenUrlMap) {
  const violations = [];
  const seen = new Set();

  for (const page of sourcePages) {
    for (const link of extractLinks(page.content)) {
      const normalizedUrl = normalizeLinkUrl(link.url);

      if (!normalizedUrl || !hiddenUrlMap.has(normalizedUrl)) {
        continue;
      }

      for (const target of hiddenUrlMap.get(normalizedUrl)) {
        const key = [
          page.repoPath,
          link.index,
          link.url,
          normalizedUrl,
          target.repoPath,
        ].join("|");

        if (seen.has(key)) {
          continue;
        }

        seen.add(key);
        violations.push({
          sourcePath: page.repoPath,
          line: lineNumberForIndex(page.content, link.index),
          link: link.url,
          normalizedUrl,
          targetPath: target.repoPath,
          reasons: target.reasons,
        });
      }
    }
  }

  return violations.sort((a, b) => {
    return (
      a.sourcePath.localeCompare(b.sourcePath) ||
      a.line - b.line ||
      a.normalizedUrl.localeCompare(b.normalizedUrl) ||
      a.targetPath.localeCompare(b.targetPath)
    );
  });
}

function extractLinks(content) {
  const maskedContent = maskFencedCodeBlocks(content);
  const links = [];
  const markdownLinkPattern = /(!?)\[[^\]]*]\(\s*([^) \t\n]+)(?:\s+["'][^"']*["'])?\s*\)/g;
  const propLinkPattern = /\b(?:href|url)=["']([^"']+)["']/g;
  const bracedPropLinkPattern = /\b(?:href|url)=\{\s*["']([^"']+)["']\s*}/g;

  collectRegexLinks(markdownLinkPattern, maskedContent, links, 2, (match) => match[1] !== "!");
  collectRegexLinks(propLinkPattern, maskedContent, links, 1);
  collectRegexLinks(bracedPropLinkPattern, maskedContent, links, 1);

  return links;
}

function collectRegexLinks(pattern, content, links, urlGroup, shouldInclude = () => true) {
  for (const match of content.matchAll(pattern)) {
    if (!shouldInclude(match)) {
      continue;
    }

    links.push({
      url: match[urlGroup],
      index: match.index,
    });
  }
}

function maskFencedCodeBlocks(content) {
  return content.replace(/(^|\n)(```|~~~)[^\n]*[\s\S]*?\n\2[^\n]*(?=\n|$)/g, (match) => {
    return match.replace(/[^\n]/g, " ");
  });
}

function normalizeLinkUrl(rawUrl) {
  const trimmedUrl = rawUrl.trim();

  if (
    !trimmedUrl ||
    trimmedUrl.startsWith("#") ||
    trimmedUrl.startsWith("mailto:") ||
    trimmedUrl.startsWith("tel:") ||
    trimmedUrl.startsWith("//")
  ) {
    return null;
  }

  if (/^https?:\/\//.test(trimmedUrl)) {
    try {
      const parsedUrl = new URL(trimmedUrl);
      if (parsedUrl.hostname !== "docs.cohere.com") {
        return null;
      }

      return normalizePathOnlyUrl(parsedUrl.pathname);
    } catch {
      return null;
    }
  }

  if (/^[a-zA-Z][a-zA-Z\d+.-]*:/.test(trimmedUrl)) {
    return null;
  }

  if (!trimmedUrl.startsWith("/")) {
    return null;
  }

  return normalizePathOnlyUrl(trimmedUrl);
}

function normalizePathOnlyUrl(rawUrl) {
  if (!rawUrl) {
    return null;
  }

  let normalizedUrl = rawUrl.trim().replace(/[?#].*$/, "");

  try {
    normalizedUrl = decodeURI(normalizedUrl);
  } catch {
    // Keep the original value if it is not a valid encoded URI.
  }

  normalizedUrl = normalizedUrl.replace(/\/+$/, "");

  if (!normalizedUrl.startsWith("/")) {
    normalizedUrl = `/${normalizedUrl}`;
  }

  return normalizedUrl || "/";
}

function lineNumberForIndex(content, index) {
  return content.slice(0, index).split(/\r?\n/).length;
}

async function writeReport(violations, hiddenPages, sourcePages) {
  const report = [
    "# Hidden Link Report",
    "",
    `Generated: ${new Date().toISOString()}`,
    "",
    `Hidden pages found: ${hiddenPages.size}`,
    `Visible source pages scanned: ${sourcePages.length}`,
    `Hidden-link violations found: ${violations.length}`,
    "",
  ];

  if (violations.length === 0) {
    report.push("No hidden links found.", "");
  } else {
    let currentSource = null;

    for (const violation of violations) {
      if (violation.sourcePath !== currentSource) {
        currentSource = violation.sourcePath;
        report.push(`## \`${currentSource}\``, "");
      }

      report.push(
        `- Line ${violation.line}: links to hidden page \`${escapeBackticks(violation.normalizedUrl)}\``,
        `  - Target: \`${escapeBackticks(violation.targetPath)}\``,
        `  - Link: \`${escapeBackticks(violation.link)}\``,
        `  - Hidden by: ${violation.reasons.map(escapeBackticks).join("; ")}`,
        ""
      );
    }
  }

  await fs.mkdir(path.dirname(reportPath), { recursive: true });
  await fs.writeFile(reportPath, `${report.join("\n")}\n`);
}

function escapeBackticks(value) {
  return String(value).replace(/`/g, "\\`");
}

(async () => {
  const pages = await buildPageIndex();
  const { navMembership, navHidden } = await collectNavData();
  const hiddenPages = buildHiddenPages(pages, navHidden);
  const hiddenUrlMap = buildHiddenUrlMap(hiddenPages, pages, navMembership);
  const sourcePages = selectSourcePages(pages, hiddenPages);
  const violations = findViolations(sourcePages, hiddenUrlMap);

  await writeReport(violations, hiddenPages, sourcePages);

  if (violations.length > 0) {
    console.error(`Found ${violations.length} hidden-link violation(s).`);
    console.error(`Report written to ${repoRelative(reportPath)}.`);
    process.exit(1);
  }

  console.log("No hidden links found.");
  console.log(`Report written to ${repoRelative(reportPath)}.`);
})();
