from flask import Flask, jsonify


app = Flask(__name__)


rides = [
    {
        "id": 1,
        "ref_no": "RF0006",
        "date": "20/8/2018"

    },
    {
            "id": 2,
            "ref_no": "RF0008",
            "date": "12/8/2018"

    }
]


@app.route('/api/v1/rides', methods=['GET'])
def get_rides():
    return jsonify({"rides": rides}), 200


if __name__ == '__main__':
    app.run()
