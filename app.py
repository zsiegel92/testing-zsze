from flask import Flask
import os 


app = Flask(__name__)

@app.route("/")
def basic_response():
    print("Someone clicked this link!")
    return "This is a Website!"

@app.route("/click/<user>")
def name_response(user):
    print("{} clicked this link!".format(user))
    return "This is a Website!"

port = int(os.environ.get("PORT", 33507))
app.run(host='0.0.0.0', port=port)