#app1.py

from flask import Flask, render_template, request,redirect,session

app = Flask(__name__)

#set a secret key for encryption session data
app.secret_key='my_secret_key'

#dictionary to store user and password

users={
    'lalit':'1234',
    'user2':'password2'
}

#to render a login form
@app.route('/')
def view_form():
    return render_template('login.html')

# for handling get request form we can get
#the form input value by using the args attribute.
#this values after submitting you will see in the urls.
#e.g http.//127.0.0.1:5000/handle_get?username-kunal&password=1234
#this exploits dur credential so that's
#why developer prefer POST request.

@app.route('/handle_get',methods=['GET'])
def handle_get():
    if request.method == "GET":
        username = request.args['username']
        password = request.args['password']
        print(username,password)
        if username in users and users[username]== password:
            return '<h1>welcome</h1>'
        else:
            return "<h1>invalid credentails</h1>"
    else:
        return render_template('login.html')
    
if __name__ == '__main__':
    app.run()
                            

        