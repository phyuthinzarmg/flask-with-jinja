from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello form Flask"

if __name__ == "__main__":
    myapp.run(debug= True)
