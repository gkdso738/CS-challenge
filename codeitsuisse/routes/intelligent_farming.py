import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def solve(s):
    A = 0
    T = 0
    C = 0
    G = 0
    for i in range(len(s)):
        if s[i] == 'A': A += 1
        if s[i] == 'T': T += 1
        if s[i] == 'C': C += 1
        if s[i] == 'G': G += 1
    ans = ""
    while C>1:
        if A > 2:
            ans = ans + "AA"
            A -= 2
        ans = ans + "CC"
        C -= 2
    if C == 1 and A > 0 and T > 0 and G > 0:
        if A > 2:
            ans = ans + "AA"
            A -= 2
        ans = ans + "TACG"
        A -= 1
        T -= 1
        C -= 1
        G -= 1
    while A > 2 and T > 0:
        ans = ans + "AA"
        A -= 2
        ans = ans + "T"
        T -= 1
    while A > 2 and G > 0:
        ans = ans + "AA"
        A -= 2
        ans = ans + "G"
        G -= 1
    while T > 0:
        ans = ans + "T"
        T -= 1
    while G > 0:
        ans = ans + "G"
        G -= 1
    while A > 0:
        ans = ans + "A"
        A -= 1
    return ans
    

@app.route('/intelligent-farming', methods=['POST'])
def evaluate_intelligent_farming():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    for i in range(len(data["list"])):
        data["list"][i]["geneSequence"] = solve(data["list"][i]["geneSequence"])
    
    logging.info("My result :{}".format(data))
    return jsonify(data);
