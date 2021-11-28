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
    departure_date = db.Column(db.String(200))
    arrival_date = db.Column(db.String(200))
    duration = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Flight {self.id}>'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flights')
def flights():
    available_flights = Flight.query.order_by(Flight.flight_created).all()
    return render_template('flights.html', flights=available_flights)


@app.route('/flight/<int:id>')
def flight(id: int):
    founded_flight = Flight.query.get_or_404(id)
    return render_template('index.html', flight=founded_flight)


if __name__ == '__main__':
    app.run(debug=True)
