from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def index():
    return 'Hello World !'


if __name__ == "__main__":
    app.run()
