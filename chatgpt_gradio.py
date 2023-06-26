import openai
import gradio

openai.api_key = "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"

messages=[{"role": "system", "content": "You are a Programming Experst"}]

def Custom_GPT(msg):
    messages.append({"role": "user", "content": msg})
    completion  = openai.ChatCompletion.create(model='gpt-3.5-turbo',  messages=messages)
    response = completion.choices[0].message.content
    messages.append({"role": "system", "content": response})
    return response

demo = gradio.Interface(fn=cCustom_GPT, inputs="text", outputs="text", title="Coder Chatbot")

demo.launch(share=True)










