from flask import Flask, render_template, request
import requests
import ollama
from openai import OpenAI



app = Flask(__name__)
client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Send the user input to the LLaMA model and get a response
        response = get_llama_response(user_input)
        return render_template('home.html', user_input=user_input, response=response)
    return render_template('home.html', user_input='', response='')


def get_llama_response(user_input):
    completion = client.chat.completions.create(
        extra_body={},
        model="deepseek/deepseek-r1:free",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    return completion.choices[0].message.content



if __name__ == "__main__":
    app.run(debug=True)

#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