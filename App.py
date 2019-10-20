from flask import Flask
# import required modules here

# initialize database here


app = Flask(__name__)

# create your routes here


@app.route("/", methods=["GET"])
def welcome():
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
