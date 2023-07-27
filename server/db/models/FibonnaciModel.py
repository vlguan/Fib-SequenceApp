from ..db import db

class Fibonnaci(db.Model):
    __tablename__: "FibonacciNumbers"
    n = db.Column(db.Integer, primary_key=True)
    fibNum = db.Column(db.Integer)
    @staticmethod
    def insertNumbers(n, fibNum):
        new_fib = Fibonnaci(n=n, fibNum=fibNum)
        db.session.add(new_fib)
        db.session.commit()
    def getNumbers(n):
        return Fibonnaci.query.filter(
            Fibonnaci.N <= n
        ).all()
