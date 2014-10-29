from flask import Flask, render_template, redirect, request
import model
import jinja2

app = Flask(__name__)


# @app.route("/")
# def index():
#     user_list = model.session.query(model.User).limit(5).all()
#     return render_template("user_list.html", users=user_list)

@app.route("/")
def login_form():
    return render_template("login_form.html")

@app.route("/login", methods=['POST'])
def login():

    email = request.form["email"]
    password = request.form["password"]

    if not email or not password:
        return "Please enter your email and password."
     #check if user is in db, if not, redirect them to a new profile link
     #if they ARE in the system, go to list of users
     #something about adding login info to the session dictionary

     # return render_template("profile.html", email = email,
    #                                     password = password)
    return "email: %s, password: %s" % (email, password)


@app.route("/new_user")
def new_user():

    #check if user is in database.
    # if not, add user to database
    
    
    # model.connect()

    #insert email and password into database

    u = model.User()
    
    #set attribute, name, to email
    u.email = request.form["email"]
    u.password = request.form["password"]

    model.session.add(u)
    model.session.commit()

    return ""


if __name__ == "__main__":
    app.run(debug=True)