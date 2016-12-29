from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'OSPA',
        'description': u'This is ospaf-api test',
        'done': False
    },
    {
        'id': 2,
        'title': u'Garvin',
        'description': u'I am garvin',
        'done': False
    }
]


@app.route('/')
def home():
    response = app.make_response(jsonify({'tasks': tasks}))
    response.status = 'False'
    return response


if __name__ == '__main__':
    app.run(port=8000, debug=True)