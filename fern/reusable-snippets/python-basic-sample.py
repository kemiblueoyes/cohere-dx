res = co.chat(
    model="command-a-plus-05-2026",
    messages=[
        {
            "role": "user",
            "content": "Who discovered gravity?",
        }
    ],
)
print(res.message.content[0].text)