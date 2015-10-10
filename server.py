from flask import Flask, request, render_template
from check_for_updates import update_check
import fantasyprodata


app = Flask(__name__)
app.debug = True


@app.before_request
def before_request():
    update_check()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
