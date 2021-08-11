from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {
        'hotel_id': 1,
        'nome': 'Alpha Um',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro',
    },
    {
        'hotel_id': 2,
        'nome': 'Alpha Dois',
        'estrelas': 4.3,
        'diaria': 430.34,
        'cidade': 'São Paulo',
    },
    {
        'hotel_id': 3,
        'nome': 'Alpha Tres',
        'estrelas': 4.3,
        'diaria': 440.34,
        'cidade': 'Curitiba',
    },
    {
        'hotel_id': 4,
        'nome': 'Alpha Quatro',
        'estrelas': 4.3,
        'diaria': 450.34,
        'cidade': 'Teresina'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


api.add_resource(Hoteis, '/hoteis')


if __name__ == '__main__':
    app.run(debug=True)