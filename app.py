from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data_list=data_list)

@app.route('/static/css/idxsty.css')
def static_file():
    return send_file('static/css/idxsty.css')

@app.route('/login.html')
def login():
    return render_template('login.html')
    
@app.route('/write.html')
def write():
    return render_template('write.html')

@app.route('/feed.html')
def feed():
    return render_template('feed.html')

@app.route('/ctrct.html')
def ctrct():
    return send_file('static/css/cntrsty.css')

@app.route('/write_ok.php', methods=['POST'])
def write_ok():
    # write_ok.php를 실행합니다.
    return os.system('php write_ok.php')

@app.route('/', methods=['POST'])
def index_post():
    title = request.form['title']
    content = request.form['content']

    # write.php를 실행합니다.
    return os.system('php write.php')

if __name__ == '__main__':
    app.run()

import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="0228", db="board", charset="utf8")
cur = db.cursor()

sql = "SELECT * from board"
cur.execute(sql)

data_list = cur.fetchall()

print(data_list[0])
print(data_list[1])
print(data_list[2])