from flask import Flask, Flaskapp01 

app01= Flask(__name__)

@app01.route('/ghar/lalit/pandey')
def hello_homes():
    return "<h1>Hello I am inside the home </h1> , <b>Lalit Pandey</b>"


if __name__ == '__maine__':
    app01.run(debug = True)