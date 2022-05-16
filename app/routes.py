from pickle import GET
from flask import render_template, flash
from flask import request
from app import myapp


@myapp.route("/",methods=['GET','POST'])
def home():
    name = 'Sarah'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    if request.method == 'GET':
        return render_template('home.html', name=name, cities=city_names)
    if request.method == 'POST':
        input = request.form["input"]
        flash(input)
        return render_template('home.html',name=name,cities=city_names)
    