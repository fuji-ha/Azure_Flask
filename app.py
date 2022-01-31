from flask import Flask,render_template,session, request, redirect, url_for

# インスタンスの作成
app = Flask(__name__)

# メイン
@app.route('/')
def index():
    return 'Hello demo'

@app.route('/kaminari')
def kaminari():
    return '雷鳴'

## 実行
if __name__ == "__main__":
    app.run(debug=True)