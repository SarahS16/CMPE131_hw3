from unicodedata import name
from flask import Flask 

my_obj = Flask(__name__)

@my_obj.route("/")
def home():
    name = 'Sarah'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    first_half = '''
    <html>
    <head>
        <body>
        <h1> Welcome ''' + name + ''' </h1>
        <a href="https://www.google.com"> not google </a>
        <ul> 
            '''
    for city in city_names:
        first_half += '''<li>'''+str(city)+'''</li>'''
    second_half = '''
        </ul>
        </body>
    </head>
    </html> '''
    first_half += second_half
    return first_half
    

my_obj.run()
