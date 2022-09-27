# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:18:28 2022

@author: Madzh
"""

from flask import Flask,redirect,url_for,request
app=Flask(__name__)

@app.route('/success/<name>/<name1>/<name2>/<name3>')
def success(name,name1,name2,name3):
    return "Welcome %s " %name +"  He studied %s " %name1 +"  His age is %s " %name2 +"  Email id %s " %name3
@app.route('/login',methods=["POST","GET"])
def login():
    
    if request.method=="POST":
        user=request.form["no"]
        user1=request.form["no1"]
        user2=request.form["no2"]
        user3=request.form["no3"]
        return redirect(url_for('success',name=user,name1=user1,name2=user2,name3=user3))

       
     
    

if __name__=='__main__':
    app.run(debug=True)

