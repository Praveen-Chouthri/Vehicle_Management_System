from flask import Flask, render_template, request, redirect, url_for
from database import check_user, add_user  
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback_default_key")  

if not app.secret_key:
    raise ValueError("FLASK_SECRET_KEY is missing in the environment variables.")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/cycle")
def cycle():
    return "Cycle Page"


@app.route("/login", methods=["POST"])
def login():
    driver_id = request.form.get("login-userid")
    password = request.form.get("login-password")

    if check_user(driver_id, password):
        return redirect(url_for("profile"))  
    return "Wrong ID or Password", 401  

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form.get("signup-name")
    age = request.form.get("signup-age")
    driver_id = request.form.get("signup-driverid")
    password = request.form.get("signup-password")
    confirm_password = request.form.get("signup-confirm-password")
    keyword = request.form.get("signup-keyword")

    if password != confirm_password:
        return "Passwords do not match", 400  

    add_user(name, age, driver_id, password, keyword)
    return redirect(url_for("profile"))  

if __name__ == "__main__":
    app.run(debug=True)

