import os
import openai
import gradio as gr

openai.api_key = os.environ.get("OPENAI_API_KEY") #implemented such that my api key is not public
messages = [{"role": "system", "content": "You are an experienced fitness coach and personal trainer"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

custom_css = """
body {
    background-color: #f5f7fa;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
.gradio-container {
    background-color: #000000;
    border: 2px solid #828282;
    border-radius: 15px;
    padding: 20px;
    margin: 20px auto;
    max-width: 600px;
}
h1 {
    color: #007acc;
    text-align: center;
}
input, textarea {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
}
Button {
    background-color: #007acc;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
}
button:hover {
    background-color: #005f99;
}
"""

with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("# Fitness Coach Chatbot")
    gr.Markdown("Welcome to your personal fitness assistant. Ask your questions below and get professional advice.")
    with gr.Row():
        user_input = gr.Textbox(placeholder="Type your message here...", label="Your Question", lines=2)
        send_btn = gr.Button("Send")
    chat_output = gr.Textbox(label="Chatbot Response") 
    gr.Image(interactive=False, value="gym.jpg")
    
    send_btn.click(fn=CustomChatGPT, inputs=user_input, outputs=chat_output)

demo.launch(share=True)
