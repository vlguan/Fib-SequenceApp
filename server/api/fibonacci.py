from flask import jsonify, request

from api import api
from db.db import db
from db.models.FibonnaciModel import FibonacciNumbers


def fibo(start, target):
        a, b = start[-2], start[-1]
        print(a,b)
        fib_sequence = start
        while len(fib_sequence) < target:
            next_fib = a + b
            fib_sequence.append(next_fib)
            a, b = b, next_fib
        return fib_sequence

@api.get("/fib")
def calculate_fib():
    query_params = request.args.to_dict()
    n = int(query_params["n"])
    fib = FibonacciNumbers.getNumbers(n)
    final = []
    if fib != []:
        for i in range(len(fib)):
            final.append(fib[i].fib_num)
    if fib == []:
        # no numbers in look up table
        final = fibo([0, 1], n)
        for i in range(len(final)):
            FibonacciNumbers.insertNumbers(i + 1, final[i])
        return jsonify(final)
    elif fib[-1].N == n:
        return jsonify(final)
    else:
        # numbers in look up table but doesnt full reach n
        result = fibo(final, n)
        # store numbers between
        for i in range(len(fib), n):
            FibonacciNumbers.insertNumbers(i + 1, result[i])
        return jsonify(result)
    
