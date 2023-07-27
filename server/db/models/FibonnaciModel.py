from ..db import db

class FibonacciNumbers(db.Model):
    __tablename__: 'FibonacciNumbers'
    N = db.Column(db.Integer, primary_key=True)
    fib_num = db.Column(db.Integer)
    @staticmethod
    def insertNumbers(n, fibNum):
        new_fib = FibonacciNumbers(N=n, fib_num=fibNum)
        db.session.add(new_fib)
        db.session.commit()
    def getNumbers(n):
        return FibonacciNumbers.query.filter(
            FibonacciNumbers.N <= n
        ).all()
