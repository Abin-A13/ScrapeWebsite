from flask import Flask, render_template
from model import Flat
from extensions import db
from os import environ


app = Flask(__name__)

# Define a list of 500 items for demonstration purposes



@app.route('/')
def index():
    flats = []

    for flat in db.session.query(Flat).all():
        del flat.__dict__['_sa_instance_state']
        flats.append(flat.__dict__)
    return render_template('home.html')


if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
    app.run(debug=True)
