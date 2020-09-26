import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

gr = []
vis = []


def dfs(x, y):
    global vis, gr
    # print("dfs", x, y)
    vis[x][y] = 1
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    for i in range(8):
        if 0<=x+dx[i] and x+dx[i]<len(gr) and 0<=y+dy[i] and y+dy[i]<len(gr[0]):
            if gr[x+dx[i]][y+dy[i]] != "*" and vis[x+dx[i]][y+dy[i]] == 0:
                dfs(x+dx[i], y+dy[i])
    

def get_ans():
    global vis, gr
    for i in range(len(gr)):
        temp = []
        for j in range(len(gr[0])):
            temp.append(0)
        vis.append(temp)
        
    ans = 0
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            if vis[i][j] == 0 and gr[i][j] == "1":
                ans += 1
                dfs(i, j)
                
    return ans



@app.route('/cluster', methods=['POST'])
def evaluate_cluster():
    
    global gr,vis
    
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    gr = data
    result = get_ans()
    
    # logging.info("My result :{}".format(result))
    return jsonify({"answer": result});
