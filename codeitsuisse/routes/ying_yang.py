import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def to_int(bit_arr):
    ans = 0
    for i in range(len(bit_arr)):
        ans = ans * 2 + bit_arr[i]
    return ans
def solve(n,k):
    dp = []
    for i in range(n+1):
        foo = []
        for j in range(k+1):
            foo.append(0)
        dp.append(foo)
    for l in range(1,k+1):
        for i in range(1,n+1):
            bit_arr = []
            x = i
            while x > 0:
                bit_arr.append(x % 2)
                x = x // 2
            sum = 0.0
            for j in range(len(bit_arr)):
                first = bit_arr[j] + dp[to_int(bit_arr[:j]+bit_arr[j+1:])][l-1]
                x = len(bit_arr)-j-1
                second = bit_arr[x] + dp[to_int(bit_arr[:x]+bit_arr[x+1:])][l-1]
                sum += max(first,second)
            dp[i] = sum / len(bit_arr)
    return dp[n][k]
def formatting(s):
    sum = 0
    for i in range(len(s)):
        sum = sum * 2
        if s[i] == 'Y': sum += 1
    return sum 


@app.route('/ying-yang', methods=['POST'])
def evaluate_ying_yang():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    n = data["number_of_elements"]
    k = data["number_of_operations"]
    s = data["elements"]      
    val = formatting(s)
    result = solve(val,k)
    # logging.info("My result :{}".format(result))
    return jsonify(result);
