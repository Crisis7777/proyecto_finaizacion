from flask import render_template, request
from database.db import *
from controller.admin_s3 import *

def func_home_page():
    return render_template("home.html")
    
def func_register_page():
    return render_template("register.html")

def func_consult_page():
    return render_template("consult.html")

def func_register_user():
    id = request.form["id"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    birthday = request.form["birthday"]
    photo = request.files["photo"]
    confirm_user = add_user(id, name, lastname, birthday)
    if confirm_user:
        s3_resource = connection_s3()
        photo_path_local = save_file(photo)
        confirm_photo = upload_file(s3_resource, photo, photo_path_local, id)
        if confirm_photo:
            return "<h1>The user and the photo were saved succesfully</h1>"
        else:
            return "<h1>The user was saved without photo</h1>"
    else:
        return "<h1>Error: The user was not created</h1>"
        
def func_consult_user():
    obj_user = request.get_json()
    id = obj_user["id"]
    result_data = consult_user(id)
    if result_data != False and len(result_data) != 0:
        s3_resource = connection_s3()
        file_found = consult_file(s3_resource, id)
        if file_found != None:
            url_file = "https://files-cym.s3.us-east-2.amazonaws.com/" + file_found
        else:
            url_file = ""
        response = {
                'status': "ok",
                'name': result_data[0][1],
                'lastname': result_data[0][2],
                'birthday': result_data[0][3],
                'photo': url_file
            }
    else:
        response = {
            'status':"error"
        }
    
    return response
    