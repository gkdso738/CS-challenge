import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def get_t(a,b,c,x,y,u,v):
    return -(a*x + b*y + c) / (a*(u-x) + b*(v-y))

def get_line(x,y,u,v):
    return (v-y), (x-u), y*u-x*v

def get_intersect(a,b,c,x,y,u,v):
    t = get_t(a,b,c,x,y,u,v)
    if t <= 1.0 and t >= 0.0:
        return x + t * (u-x), y + t * (v-y)
    return np.nan(), np.nan()

def solve(n,a,b,c,cood_x,cood_y):
    ans = []
    for i in range(n):
        x, y = get_intersect(a,b,c,cood_x[i],cood_y[i],cood_x[i+1],cood_y[i+1])
        if x != np.nan():
            ans.append({"x": x, "y": y})
    return ans


@app.route('/revisitgeometry', methods=['POST'])
def evaluate_revisitgeometry():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    st_x, st_y = data["lineCoordinates"]["x"], data["lineCoordinates"]["y"]
    st_u, st_v = data["lineCoordinates"]["x"], data["lineCoordinates"]["y"]
    a,b,c = get_line(float(st_x),float(st_y),float(st_u),float(st_v))
    cood_x = []
    cood_y = []
    for elements in data['shapeCoordinates']:
        x = elements["x"]
        y = elements["y"]
        cood_x.append(float(x))
        cood_y.append(float(y))
    cood_x.append(cood_x[0])
    cood_y.append(cood_y[0])
    result = solve(n,a,b,c,cood_x,cood_y)
    logging.info("My result :{}".format(result))
    return jsonify({"result": result});
