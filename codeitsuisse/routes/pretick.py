import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


def read(ln):
    lines = ln.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
    columns = lines[0]
    lines.remove(lines[0])
    return lines

def last_px(lines):
    return lines[len(lines)-1][3]

@app.route('/pre-tick', methods=['POST'])
def evaluate_pretick():
    data = request.get_data();
    logging.info("data sent for evaluation {}".format(data))

    lines = read(data)
    result = last_px(lines)
    # logging.info("My result :{}".format(result))
    return jsonify(result);
