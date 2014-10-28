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

    return "email: %s, password: %s" % (email, password)

    #check if user is in database.
    # if not, add user to database
    # return render_template("profile.html", email = email,
    #                                     password = password)



if __name__ == "__main__":
    app.run(debug=True)