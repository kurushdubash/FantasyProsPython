from flask import Flask, request, render_template
import os
#import fantasyprodata


app = Flask(__name__)
app.debug = True
app.secret_key = 'development'

@app.before_request
def before_request():
    os.system('bash download.sh')       


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.debug = True
    app.run()
