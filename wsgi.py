from flask import Flask
import time

application = Flask(__name__)
start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/test")
def test():
    return "Testing!"

@application.route("/testprobe")
def test():
    return "I'm alive\nSince: {}".format(start_time)



if __name__ == "__main__":
    application.run()
