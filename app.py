from flask import Flask,render_template,session, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello demo'

## 実行
if __name__ == "__main__":
    app.run(debug=True)