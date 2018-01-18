from flask import Flask
import time

start_time = None
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/test")
def test():
    return "Testing!"

@application.route("/probe")
def test():
    return "I'm alive\nSince: {}".format(start_time)



if __name__ == "__main__":
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    application.run()
