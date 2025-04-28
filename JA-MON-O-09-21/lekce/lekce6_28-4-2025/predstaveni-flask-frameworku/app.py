from flask import Flask

app = Flask(__name__)

# domovska stranka
@app.route("/")
def main():
    return "Hello world"


if __name__ == '__main__':
    app.run(debug=True)