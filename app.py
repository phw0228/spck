from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/css/idxsty.css')
def static_file():
    return send_file('static/css/idxsty.css')

@app.route('/templates/login.html')
def login():
    return render_template('login.html')

@app.route('/templates/feed.html')
def feed():
    return render_template('feed.html')

if __name__ == '__main__':
    app.run()

