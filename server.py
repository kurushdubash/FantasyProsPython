from flask import Flask, request, render_template
from check_for_updates import update_check
from fantasyprodata import get_all_players

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

@app.route('/rankings', methods=['POST'])
def rankings():
    postition = request.form["action"]
    print(postition)
    player = get_all_players(postition)
    print(player)
    return render_template('rankings.html', updated=last_updated, type=postition, data=player)


if __name__ == "__main__":
    app.debug = True
    app.run()
