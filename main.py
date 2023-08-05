from flask import Flask
import codecs

main_page = codecs.open("./entry_page.html", 'r', 'utf-8')


app = Flask(__name__)

@app.route("/")
def hello_world():
    return main_page

app.run(host='0.0.0.0', debug=True, port=12345, use_reloader=True)
