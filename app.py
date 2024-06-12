from flask import Flask, request, render_template
import os

app = Flask(__name__)

# 设置一个简单的路由来渲染首页
@app.route('/')
def index():
    return render_template('index.html')

# 设置一个路由来处理表单提交
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # 处理表单数据，例如存储在文件或数据库中
    with open('messages.txt', 'a') as f:
        f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")

    return "感謝您的聯繫，我們會儘快回覆您！"

if __name__ == '__main__':
    app.run(debug=True)
