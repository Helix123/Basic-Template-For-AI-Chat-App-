from flask import Flask, render_template, request
import openai
import time
import json

# Set up OpenAI API credentials
openai.api_key = "your openai api key"

# Set up the character name you want to chat with
character_name = "Shirone"

app = Flask(__name__)

# Define the function to generate a response from ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

# Define the function to start the chat with the character
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get("msg")
    prompt = f"{character_name}: {user_input}\nYou:"
    response = generate_response(prompt)
    time.sleep(1)
    return json.dumps(response)


if __name__ == "__main__":
    app.run(debug=True)
