import numpy as np
import sys
from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_restful import Resource

app = Flask(__name__)
api = Api(app)


class Predict(Resource):
    def get(self):
        r = np.random.rand()
        result = {
            'probability': r,
            'label': float(r > 0.5),
        }
        return jsonify(**result)


api.add_resource(Predict, '/api/v1/predict')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        host = "0.0.0.0"
        port = None

    app.run(host=host, port=port, debug=False)
