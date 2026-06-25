import cohere

co = cohere.OciClientV2(
    oci_region="us-chicago-1",
    oci_compartment_id="ocid1.compartment.oc1...",
)