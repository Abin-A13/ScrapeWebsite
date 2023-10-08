from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object("config.Config")

db = SQLAlchemy(app)



class Flat(db.Model):
    __tablename__ = "flat"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=False, nullable=False)
    image_url = db.Column(db.String(255), unique=False, nullable=True)

    def __init__(self, title, image_url):
        self.title = title
        self.image_url = image_url


@app.route('/')
def index():
    flats = []

    for flat in db.session.query(Flat).all():
        del flat.__dict__['_sa_instance_state']
        flats.append(flat.__dict__)
    return render_template('home.html')


