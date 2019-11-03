# # import modules

# from flask import Flask, render_template, request
# from flask_pymongo import PyMongo
# # initialize database


# # create your routes here

# # initializes app

# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://shawn:18740811@h4iminihack-73gfh.mongodb.net/test?retryWrites=true&w=majority"
# #app.config["MONGO_URI"] = "mongodb://localhost:27017/socialMedia"

# mongo = PyMongo(app)
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=4000, debug=True)

from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('home.html',title='Community speak', posts=posts)

# @app.route('/about')
# def about():
#     return render_template('community.html', title='Community speak', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)