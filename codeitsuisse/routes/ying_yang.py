import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;
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
def solve(n,ln,k):
    if ln > 15: return 0
    dp = []
    for i in range(int(2**ln)):
        tmp = []
        for l in range(ln+1):
            foo = []
            for j in range(k+1):
                foo.append(0)
            tmp.append(foo)
        dp.append(tmp)
    for l in range(1,k+1):
        for u in range(1,ln+1):
            for i in range(1,int(2**ln)):
                bit_arr = []
                x = i
                for _ in range(u):
                    bit_arr.append(x % 2)
                    x = x // 2
                sum = 0.0
                for j in range(u):
                    first = bit_arr[j] + dp[to_int(bit_arr[:j]+bit_arr[j+1:])][u-1][l-1]
                    x = u-j-1
                    second = bit_arr[x] + dp[to_int(bit_arr[:x]+bit_arr[x+1:])][u-1][l-1]
                    sum += max(first,second)
                dp[i][u][l] = sum / u
    return dp[n][ln][k]
def formatting(s):
    sum = 0
    for i in range(len(s)):
        sum = sum * 2
        if s[i] == 'Y': sum += 1
    return sum


@app.route('/yin-yang', methods=['POST'])
def evaluate_ying_yang():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    n = data["number_of_elements"]
    k = data["number_of_operations"]
    s = data["elements"]
    val = formatting(s)
    result = solve(val,n,k)
    logging.info("My result :{}".format(result))
    return jsonify(result);

