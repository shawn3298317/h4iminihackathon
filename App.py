# # import modules

from flask import Flask, render_template, url_for, request
from flask_pymongo import PyMongo

# initializes app

app = Flask(__name__)
# initialize database
app.config["MONGO_URI"] = "mongodb+srv://shawn:18740811@h4iminihack-73gfh.mongodb.net/test?retryWrites=true&w=majority"

posts = [
    {
        'author':'Rahul Suresh',
        'content':'First post content',
        'date_posted':'April 20, 2018'
    }, 
    {
        'author':'Akari',
        'content':'I\'m glad you do',
        'date_posted':'April 21, 2018'
    }
]

# create your routes here

@app.route('/')
def home():
    return render_template('home.html',title='Community speak', posts=posts)

# @app.route('/about')
# def about():
#     return render_template('community.html', title='Community speak', posts=posts)

@app.route("/login", methods=["GET", "POST", "PUT"])
def login():
	"""Serve login page template."""
	return render_template("login.html")

mongo = PyMongo(app)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)

# if __name__ == '__main__':
#     app.run(debug=True)