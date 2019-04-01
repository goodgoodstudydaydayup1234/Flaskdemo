from flask import Flask,render_template,request,redirect,make_response
import datetime
from orm import model
from orm import ormmanage as manage

app = Flask(__name__)
app.debug=True
app.send_file_max_age_default=datetime.timedelta(seconds=1)

# b1 = model.Book()
# b1.id = 1
# b1.name = '三体'
# b1.price = 45
# b2 = model.Book()
# b2.id = 2
# b2.name = '皮囊'
# b2.price = 50
# b3 = model.Book()
# b3.id = 3
# b3.name = '边城'
# b3.price = 40

# 将http://127.0.0.1:5000/ 和index视图函数绑定
@app.route('/')
def index():

    user = None
    user = request.cookies.get('name')
    # print(user)
    if user:
        print('之前登过')
    else:
        print('之前没登过')
    return render_template('index.html',userinfo=user)


@app.route('/regist',methods=['POST','GET'])
def regist():
    if request.method == 'GET':
        # args = request.args
        # name = args.get('name')
        # we = args.get('we')
        # print(name,we)
        # print('收到get请求，返回注册页面')
        return render_template('regist.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(username,password)
        # print('收到post请求，可以提取表单数据')
        # print('注册成功')
        try:
            manage.insertUser(username, password)
            return redirect('/login')
        except:
            redirect('/regist')


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            # print('登录成功')
            result = manage.checkUser(username,password)
            # 为了让响应可以携带头信息，需要构造响应
            # return '123'
            res = make_response(redirect('/goods'))
            res.set_cookie('name',username,expires=datetime.datetime.now()+datetime.timedelta(days=100))
            return res
        except:
            return  redirect('/login')


@app.route('/quit')
def quit():
    res = make_response(redirect('/'))
    res.delete_cookie('name')
    return res


@app.route('/goods',methods=['POST','GET'])
def goods():
    user = None
    user = request.cookies.get('name')
    return render_template('goods.html',infoarray=[1,2,3,4,5,6,7,8,9],userinfo=user)


@app.route('/detial/<id>')
def detial(id):
    # print(id)
    user = None
    user = request.cookies.get('name')
    return render_template('detial.html',detial='very good',id=id,userinfo=user)



if __name__ == "__main__":
    app.run()
