from flask import Flask
import main

app = Flask(__name__)


@app.route('/')
def less():
    return ''


@app.route('/get_champions/<champion>')
def find(champion):
    temp = main.get_champions_info_by_dict(champion)

    return temp


if __name__ == "__main__":
    app.run()
