import logging
import json
import numpy as np
import pandas as pd

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


def read(ln):
    lines = ln.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
    columns = lines[0]
    lines.remove(lines[0])
    df = pd.DataFrame(lines, columns=columns)
    return df

def last_px(df):
    return df.loc[len(df)-1,'Close']

@app.route('/pre-tick', methods=['POST'])
def evaluate_pretick():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    df = read(data)
    result = last_px(df)
    # logging.info("My result :{}".format(result))
    return jsonify(result);
