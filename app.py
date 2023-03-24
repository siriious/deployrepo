from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "hii"

app.run(debug=True)

