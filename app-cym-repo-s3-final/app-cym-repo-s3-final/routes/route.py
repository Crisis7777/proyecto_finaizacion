from controller.control import *
from server import app

@app.route("/")
def home_page():
    return func_home_page()
    
@app.route("/register_page")
def register_page():
    return func_register_page()

@app.route("/consult_page")
def consult_page():
    return func_consult_page()

@app.route("/register_user", methods=["post"])
def register_user():
    return func_register_user()
    
@app.route("/consult_user", methods=["post"])
def consult_user():
    return func_consult_user()