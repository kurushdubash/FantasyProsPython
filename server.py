from flask import Flask, request, render_template
from check_for_updates import update_check
from fantasyprodata import get_all_players
import json
import html.parser
parser = html.parser.HTMLParser()


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
    player = [{'rank':.5}]
    player+=get_all_players(postition)
    player.append({'rank':len(player)})
    test = '['
    for item in player:
        test+=(json.dumps(item)) + ', '
    test += ']'
    print(test)
    test = parser.unescape(test)
    return render_template('rankings.html', updated=last_updated, type=postition, data=test)


if __name__ == "__main__":
    app.debug = True
    app.run()
