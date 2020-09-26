import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/slsm', methods=['POST'])
def evaluate_slsm():
    
    global n, m, gr
    
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    n = len(data)
    m = len(data[0])
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(data[i][j])
        gr.append(temp)
    
    result = get_ans()
    
    # logging.info("My result :{}".format(result))
    return jsonify({"answer": result});

