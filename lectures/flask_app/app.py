from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def read_root():
    return jsonify('hello world')


if __name__ == '__main__':
    app.run()
