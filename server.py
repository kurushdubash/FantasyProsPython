from flask import Flask, request, render_template
from check_for_updates import update_check
import fantasyprodata


app = Flask(__name__)
app.debug = True

last_updated = update_check()

# @app.before_request
# def before_request():
#     last_updated = update_check()
#     print(last_updated)

@app.route('/')
def index():
    return render_template('index.html', updated=last_updated)

if __name__ == "__main__":
    app.debug = True
    app.run()
