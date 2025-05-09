from flask import Flask, render_template, request, redirect, session, url_for
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = 'secretkey123'

USER_API = os.getenv("USER_API_URL")
APPT_API = os.getenv("APPT_API_URL")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = {
            "email": request.form["email"],
            "password": request.form["password"]
        }
        res = requests.post(f"{USER_API}/login", json=data)
        if res.status_code == 200:
            session["token"] = res.json()["access_token"]
            return redirect(url_for("appointments"))
    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = {
            "email": request.form["email"],
            "password": request.form["password"]
        }
        res = requests.post(f"{USER_API}/register", json=data)
        if res.status_code == 200:
            return redirect("/login")
    return render_template("register.html")

@app.route('/appointments')
def appointments():
    token = session.get("token")
    if not token:
        return redirect("/login")
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(APPT_API, headers=headers)
    return render_template("appointments.html", appointments=res.json())

@app.route('/appointments/create', methods=["POST"])
def create_appointment():
    token = session.get("token")
    if not token:
        return redirect("/login")
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "scheduledTime": request.form["scheduledTime"]
    }
    res = requests.post(APPT_API, json=body, headers=headers)
    return redirect("/appointments")

@app.route('/appointments/update', methods=["POST"])
def update_appointment():
    token = session.get("token")
    if not token:
        return redirect("/login")
    headers = {"Authorization": f"Bearer {token}"}
    appt_id = request.form["id"]
    body = {
        "id": appt_id,
        "scheduledTime": request.form["scheduledTime"]
    }
    requests.put(f"{APPT_API}/{appt_id}", json=body, headers=headers)
    return redirect("/appointments")

@app.route('/appointments/delete', methods=["POST"])
def delete_appointment():
    token = session.get("token")
    if not token:
        return redirect("/login")
    headers = {"Authorization": f"Bearer {token}"}
    appt_id = request.form["id"]
    requests.delete(f"{APPT_API}/{appt_id}", headers=headers)
    return redirect("/appointments")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)