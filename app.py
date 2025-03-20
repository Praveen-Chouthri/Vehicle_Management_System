from flask import Flask, render_template, request, redirect, url_for
from database import check_user, add_user  # Move imports to the top
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY_FLASK", "fallback_default_key")  # Store securely in production

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

"""from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('profile.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/cycle")
def cycle():
    return render_template('cycle.html')

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)"""


"""
from flask import Flask, render_template, request, redirect, session
from database import check_user  # Import database functions
import os

app = Flask(__name__)
app.secret_key =  os.getenv("SECRET_KEY","fallback_default_key") # Needed for session handling

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    if "user" in session:
        return render_template("profile.html", user=session["user"])
    return redirect("/")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["signup-name"]
    age = request.form["signup-age"]
    driver_id = request.form["signup-driverid"]
    password = request.form["signup-password"]
    confirm_password = request.form["signup-confirm-password"]
    keyword = request.form["signup-keyword"]

    if password != confirm_password:
        return "Passwords do not match!", 400

    if database.register_user(name, age, driver_id, password, keyword):
        return redirect("/profile")
    else:
        return "User already exists!", 400

@app.route("/login", methods=["POST"])
def login():
    driver_id = request.form.get("login-userid")
    password = request.form.get("login-password")

    if check_user(driver_id, password):
        return redirect(url_for("profile"))  # Redirect to profile page if correct
    else:
        return "Wrong ID or Password", 401
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
"""
