import os
from flask import Flask, render_template
from flask import request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def article():
    if request.method == 'POST':
        form = request.form
        result = []
        question = form['question']
        r = requests.post(
            url="https://hf.space/embed/jaimin/content/+/api/predict",
            json={"data": [question,"En"]},
        )
        response = r.json()

        response = response['data']

        result.append(response[0])
        result.append(response[1])
        result.append(response[2])
        result.append(response[3])

        return result

    return render_template("test.html")


if __name__ == '__main__':
    app.run(debug=True)

