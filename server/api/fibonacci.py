from flask import jsonify, request

from api import api
from db.db import db
from db.models.FibonnaciModel import FibonacciNumbers
@api.get("/fib")

def calculate_fib():
    def fibo(start, target, existingLen):
        a, b = start[0], start[1]
        if(a==0):
            fib_sequence = [0,1]
        else:    
            fib_sequence= []
        while len(fib_sequence) + existingLen < target:
            next_fib = a + b
            fib_sequence.append(next_fib)
            a,b = b, next_fib
        return fib_sequence
    query_params = request.args.to_dict()
    n = int(query_params['n'])
    fib = FibonacciNumbers.getNumbers(n)
    final =[]
    if(fib == []):
        # no numbers in look up table
        final = fibo([0,1], n, 0)
        for i in range(len(final)):
            FibonacciNumbers.insertNumbers(i+1, final[i])
        return jsonify(final)
    else:
        if(fib[-1].N == n):
            for i in fib:
                final.append(i.fib_num)
            return jsonify(final)
        else:
            # numbers in look up table but doesnt full reach n
            temp = []
            final=fibo([fib[-2].fib_num,fib[-1].fib_num], n, len(fib))
            for i in fib:
                temp.append(i.fib_num)
            return jsonify(temp + final)