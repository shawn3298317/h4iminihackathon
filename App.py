from flask import Flask, render_template, request
# import required modules here
from models.Post import Post
# initialize database here

from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/socialMedia"
mongo = PyMongo(app)


# create your routes here


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        mongo.db.posts.insert(
            {"title": request.form["title"], "content": request.form["content"]})
    posts = mongo.db.posts.find()
    # render your template html here
    return render_template("home.html", posts=posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
