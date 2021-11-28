from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plane = db.Column(db.String(200), nullable=False)
    destination_from = db.Column(db.String(200), default='Лос Сантос')
    destination_to = db.Column(db.String(200), default='Сан Фіерро')
    flight_created = db.Column(db.DateTime, default=datetime.utcnow())
    departure_date = db.Column(db.DateTime)
    arrival_date = db.Column(db.DateTime)
    duration = db.Column(db.Float)
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Flight {self.id}>'


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
