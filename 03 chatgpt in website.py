import openai
import gradio

openai.api_key="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"

messages= [{"role": "system", "content": "you are a psycologist"}]

def CustomChatGPT(Type_your_question_here):
    messages.append({"role": "user", "content":Type_your_question_here})
    response =openai.ChatCompletion.create(
           model ="gpt-3.5-turbo",
           messages=messages)
    
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo= gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs="text", title ="Marwin")

demo.launch(share=True)
