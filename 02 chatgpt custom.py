import openai

openai.api_key="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"

messages = []
system_msg = input("what type of chatbot would you like to create?\n")
messages.append({"role":"system","content": system_msg})

print("your new assistant is ready")
while input != "quit()":
    message= input()
    messages.append({"role": "user", "content":message})
    response =openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply=response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content": reply})
    print("\n"+reply+"\n")
