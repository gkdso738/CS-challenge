import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/sort', methods=['POST'])
def evaluate_sort():
    data = request.get_json();
    #logging.info("data sent for evaluation {}".format(data))
    result = sorted(data)
    #logging.info("My result :{}".format(result))
    return jsonify(result);
