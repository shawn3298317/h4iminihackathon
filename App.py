# # import modules

from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
import json

from pymongo import MongoClient

# initializes app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
# initialize database
app.config["MONGO_URI"] = "mongodb+srv://shawn:18740811@h4iminihack-73gfh.mongodb.net/test?retryWrites=true&w=majority"


def add_new_user_to_db(name, email, pw):
    client = MongoClient(app.config["MONGO_URI"])
    db = client.happy
    users = db.users
    users.insert_one({"name": name, "email": email, "password": pw})

def find_user_from_db(email, pw):
    client = MongoClient(app.config["MONGO_URI"])
    db = client.happy
    users = db.users
    user = users.find_one({"email": email, "password": pw})
    print(user)
    return user

def add_new_post_to_db(post_msg, user_name):
    client = MongoClient(app.config["MONGO_URI"])
    db = client.happy
    posts = db.posts
    posts.insert_one({"name": user_name, "post_msg": post_msg})

def get_posts_from_db(topk):
    client = MongoClient(app.config["MONGO_URI"])
    db = client.happy
    posts = db.posts
    ret_posts = posts.find({})
    return ret_posts

@app.route('/', methods=["GET", "POST", "PUT"])
def home():
    # TODO: read from database
    # TODO: populate some posts in database
    posts = get_posts_from_db(topk=20)
    user_name = "Anonymous"
    if "messages" in request.args:
        user_name = request.args["messages"]

    # print("user_name", request.args["messages"])

    form = request.form
    error = None

    if request.method == "POST":
        
        # TODO: Add publish date later...
        add_new_post_to_db(form.get("new_post"), user_name)

    return render_template('home.html',title='Community speak', posts=posts, user_name =user_name)

# @app.route('/about')
# def about():
#     return render_template('community.html', title='Community speak', posts=posts)

@app.route("/login", methods=["GET", "POST", "PUT"])
def login():
    """Serve login page template."""
    form = request.form
    error = None

    if request.method == "POST":
        print(form, form.get("email"), form.get("password"))
        msg = find_user_from_db(form.get("email"), form.get("password"))
        # TODO: verify with database
        # if form.get("email") != "admin@bu.edu" or form.get("password") != "admin":
        if msg is None:
            error = "Cannot find this user. Please try again."
        else:
            return redirect(url_for('home', messages=msg["name"]))
    return render_template("login.html", error=error, form=form)

@app.route("/signup", methods=["GET", "POST", "PUT"])
def signup():
    """Serve login page template."""
    form = request.form
    error = None

    if request.method == "POST":
        print(form, form.get("name"), form.get("email"), form.get("password"))
        # TODO: add new user to database
        add_new_user_to_db(form.get("name"), form.get("email"), form.get("password"))
        return redirect(url_for('home'))
    return render_template("signup.html", error=error, form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)

# if __name__ == '__main__':
#     app.run(debug=True)