from flask import jsonify, request

from api import api
from db.models.FibonnaciModel import FibonacciNumbers


def fibo(start_sequence, target):
        a, b = start_sequence[-2], start_sequence[-1]
        print(a,b)
        fib_sequence = start_sequence
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
    final_sequence = []
    if fib != []:
        final_sequence = [f.fib_num for f in fib]
    if fib == []:
        # no numbers in look up table
        final_sequence = fibo([0, 1], n)
        for i in range(len(final_sequence)):
            FibonacciNumbers.insertNumbers(i + 1, final_sequence[i])
        return jsonify(final_sequence)
    elif fib[-1].N == n:
        return jsonify(final_sequence)
    else:
        # numbers in look up table but doesnt full reach n
        result = fibo(final_sequence, n)
        # store numbers between
        for i in range(len(fib), n):
            FibonacciNumbers.insertNumbers(i + 1, result[i])
        return jsonify(result)
    
