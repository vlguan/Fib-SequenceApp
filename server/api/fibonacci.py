from flask import jsonify, request

from api import api

@api.get("/fib")

def calculate_fib():
    def fibo(n):
        if n<=1:
            return n
        else:
            return(fibo(n-1) + fibo(n-2))
    query_params = request.args.to_dict()
    n = query_params['n']
    final = []
    for i in range(int(n)):
        final.append(fibo(i))
    return jsonify(final)