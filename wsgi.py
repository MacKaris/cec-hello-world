import socket
import time
import os.path
from flask import Flask

application = Flask(__name__)

@application.route("/hello")
def hello():    
	print ("spede")
	return "Hello Wooiorld! Greetings from "+socket.gethostname()+"\n"

@application.route("/")
def log():    

	FILE_NAME = "log"
	if (os.path.isfile(FILE_NAME)):
		with open('log', 'a') as f:
			aika=time.time()
			f.write(socket.gethostname()+" : "+str(aika)+'\n')
		f.closed
	else:
		with open('log', 'w') as f:
			aika=time.time()
			f.write(socket.gethostname()+" : "+str(aika)+'\n')
		f.closed

	with open('log', 'r') as f:
		result = f.read()
	f.closed
	return result

if __name__ == "__main__":
	application.run()
