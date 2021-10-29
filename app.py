from flask import Flask,request,render_template
import pickle
from dhooks import Webhook

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'nachi':'123','james':'aac','karthik':'asdsf'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('home.html',name=name1)

@app.route('/home', methods=['POST', 'GET'])
def webhook_sender():
    webhook_name = request.form['webhook_username']
    webhook_content = request.form['webhook_message']
    webhook_link = request.form['webhook_link']
    hook = Webhook(webhook_link)
    hook.modify(webhook_name)
    hook.send(webhook_content)


if __name__ == '__main__':
    app.run()
