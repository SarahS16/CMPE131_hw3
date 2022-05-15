from app import myapp_obj
from flask import render_template, flash

from flask_hp.app.forms import CityForm

@myapp_obj.route("/home")
def home():
    form = CityForm()
    if form.validate_on_submit():
        flash(form.city)
    name = 'Sarah'
    city_names = ['paris', 'london', 'rome']
    return render_template('home.html', name=name, cities=city_names)