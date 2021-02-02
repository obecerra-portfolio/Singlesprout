import flask

from flask import request, jsonify
from Response import createResponse
from TestData import inputData
from Validation import validationSuite

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# My signature
@app.route('/', methods=['GET'])
def home():
    return "<h1>This is my test api for SingleSprout by Omar Becerra.</p>"


# Testing my own data
@app.route('/api/v1/resources/clients/all', methods=['GET'])
def api_all():
    return jsonify(inputData)


@app.route('/api/v1/resources/client', methods=['POST'])
def api_id():
    if request.is_json:
        content = request.get_data()
        flag, message = validationSuite(content)
        if(flag):
            return jsonify(createResponse(content))
        else:
            return jsonify(message)
    else:
        return jsonify('INVALID_JSON')

    return jsonify('VALID')

@app.errorhandler(400)
def bad_request(e):
    return jsonify('INVALID_JSON')

@app.errorhandler(404)
def bad_request(e):
    return jsonify('PAGE_DOES_NOT_EXIST')

@app.errorhandler(500)
def bad_request(e):
    return jsonify('SERVER_ERROR')

app.run()
