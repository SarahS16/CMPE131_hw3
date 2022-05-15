from pickle import GET
from flask import render_template, flash
from requests import request
from app import myapp
from app.forms import CityForm

@myapp.route("/",methods=['GET','POST'])
def home():
    name = 'Sarah'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    form = CityForm(request.form)
    if request.method == 'POST' and form.validate():
        town = form.data
        flash(town)
        return render_template('home.html', name=name, cities=city_names, form=form)
    else:
        return render_template('home.html', name=name, cities=city_names, form=form)