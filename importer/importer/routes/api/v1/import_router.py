"""API ROUTER"""

import logging

from flask import jsonify, Blueprint, request
from importer.routes.api import error
from importer.validators import validate_greeting
from importer.middleware import set_something
from importer.serializers import serialize_greeting
from importer.helpers import RecipeHelper
import json
import CTRegisterMicroserviceFlask

import_endpoints = Blueprint('import_endpoints', __name__)

@import_endpoints.route('/hello', strict_slashes=False, methods=['GET'])
@set_something
@validate_greeting
def say_hello(something):
    """World Endpoint"""
    logging.info('[ROUTER]: Say Hello')
    config = {
        'uri': '/dataset',
        'method': 'GET',
    }
    response = CTRegisterMicroserviceFlask.request_to_microservice(config)
    elements = response.get('data', None) or 1
    data = {
        'word': 'hello',
        'propertyTwo': 'random',
        'propertyThree': elements,
        'something': something,
        'elements': 1
    }
    if False:
        return error(status=400, detail='Not valid')
    return jsonify(data=[serialize_greeting(data)]), 200

@import_endpoints.route('/import', strict_slashes=False, methods=['POST'])
def upload():
    """Uploads rasters to Rasdaman"""
    logging.info('[ROUTER] Importing rasters')
    logging.info("Request json data:")
    logging.info(request.json)

    
    return "OK", 200
