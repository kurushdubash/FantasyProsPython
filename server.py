from flask import Flask, request, render_template
import os, datetime
#import fantasyprodata


app = Flask(__name__)
app.debug = True
app.secret_key = 'development'

@app.before_request
def before_request():
    os.system('bash download.sh')       


@app.route('/')
def index():
    data = open('data/wr')
    j = "NULL"
    for line in data:
        if 's' in line:
            j = line
    return render_template('index.html', data=j)

@app.route('/data/wr')
def getter():
    return os.system('data/wr')



if __name__ == "__main__":
    app.debug = True
    app.run()
