from flask import  Flask,url_for,request
app=Flask(__name__)

@app.route('/')

# def hello():
#     return "<script>alert('hello Flask!!!')</script>"
def hi1():
    return "<script>alert('hello Flask1!!!')</script>"

@app.route('/index')

def index():
    with open("index.html",'rb') as file:
        data=file.read()
    return data
@app.route('/user/<username>')
def  show_user_name(username):
    return "user: %s"%username

@app.route('/post/<int:post_id>')
def  show_post_id(post_id):
    return "post id : %s"%post_id

@app.route('/url/')
def  get_url():
    return  url_for('static',filename="css/style.css") # 引入css文件
    # return url_for('show_post_id',post_id=3)

@app.route('/login')

def login():
    if request.method=='GET':
        return 'GET  request'
if __name__=='__main__':
    app.run(debug=True)

