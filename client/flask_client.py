
from flask import Flask, send_file

app = Flask(__name__)

#绑定路由('/index')的执行函数index()
@app.route('/index')
def index():
    #首页
    return send_file('templates/index.html')

@app.route('/login')
def login():
    #登录
    return send_file('templates/login.html')

@app.route('/register')
def register():
    #注册
    return send_file('templates/register.html')

@app.route('/<username>/info')
def info(username):
    #个人信息
    return send_file('templates/about.html')

@app.route('/<username>/change_info')
def change_info(username):
    #修改个人信息
    return send_file('templates/change_info.html')

@app.route('/<username>/topic/release')
def topic_release(username):
    #发表博客
    return send_file('templates/release.html')


@app.route('/<username>/topics')
def topics(username):
    #个人博客列表
    return send_file('templates/list.html')

@app.route('/<username>/topics/detail/<t_id>')
def topics_detail(username, t_id):
    #博客内容详情
    return send_file('templates/detail.html')

@app.route("/test")
def test():
    return send_file("templates/test.html")



if __name__ == '__main__':
    # 启动flask服务,
    #默认监听5000端口
    app.run(debug=True)

