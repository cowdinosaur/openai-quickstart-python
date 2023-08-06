import os
from dotenv import load_dotenv
import openai
from flask import Flask, redirect, render_template, request, url_for

load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["animal"] 
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(prompt),
            max_tokens=200,
            temperature=0.3,
        )
        return redirect(url_for("index", prompt=prompt,result=response.choices[0].text))

    result = request.args.get("result")
    prompt= request.args.get("prompt")
    return render_template("index.html", prompt=prompt, result=result)


def generate_prompt(prompt):
    return "{}".format(prompt)
