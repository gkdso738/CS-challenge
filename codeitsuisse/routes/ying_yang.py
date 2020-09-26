import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/ying-yang', methods=['POST'])
def evaluate_ying_yang():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    

    # logging.info("My result :{}".format(result))
    return jsonify({"answer": ans});
