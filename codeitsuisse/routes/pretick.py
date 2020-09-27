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
    #lines.remove(lines[len(lines)-1])
    return lines

def last_px(lines):
    return float(lines[len(lines)-1][3].strip())

@app.route('/pre-tick', methods=['POST'])
def evaluate_pretick():
    data = request.get_data();
    #logging.info("data sent for evaluation {}".format(data))

    lines = read(data.decode())
    logging.info("data sent for evaluation {}".format(lines))
    result = last_px(lines)
    logging.info("My result :{}".format(result))
    return jsonify(result);
