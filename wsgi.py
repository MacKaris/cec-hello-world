import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    return "Hello World! Greetings from "+socket.gethostname()+"\n"
    with open('log', 'w') as f:

		f.write(socket.gethostname()+", "+time.time()+'\n')
	
	    f.closed


if __name__ == "__main__":
    application.run()
