from flask import Flask
from redis import Redis
@app.route('/')
def hello():
    count = redis.incr('hits')
    return '<h1 style="color:red">Welcome to Java Home Docker APP</h1>'
    
if __name__ -- "__main__":
   app.run(host="0.0.0.0", debug=True)
