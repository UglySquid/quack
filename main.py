from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "replace this with html file name"


if __name__ == "__main__":
    app.run()