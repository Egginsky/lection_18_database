from flask import Flask, render_template, request

from models import User, db

db.create_all()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    all_users = db.query(User).all()
    return render_template("login.html", users=all_users)

@app.route("/login", methods=["POST"])
def login_2():
    print("POST endpunkt")
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    #print(name, email)
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    all_users = db.query(User).all()
    return render_template("login.html", users=all_users)


if __name__ == '__main__':
    app.run(debug=True)