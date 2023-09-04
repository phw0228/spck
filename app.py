from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/feed.html')
def feed():
    return render_template('feed.html')

@app.route('/ctrct.html')
def ctrct():
    return render_template('ctrct.html')

@app.route('/static/css/idxsty.css')
def idxsty():
    return send_file('static/css/idxsty.css')

@app.route('/static/css/cntrsty.css')
def cntrsty():0
    return send_file('static/css/cntrsty.css')

if __name__ == '__main__':
    app.run()
