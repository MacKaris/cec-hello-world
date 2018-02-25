import socket
import time
import os.path
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    	return "Hello World! Greetings from "+socket.gethostname()+"\n"
    

	FILE_NAME = "log"
	if (os.path.isfile(FILE_NAME)):
		with open('log', 'a') as f:
			aika=time.time()
			f.write("kullikulli, "+str(aika)+'\n')
		f.closed
	else:
		with open('log', 'w') as f:
			aika=time.time()
			f.write("kullikulli, "+str(aika)+'\n')
		f.closed
	
	with open('log', 'r') as f:
		for line in f:
			print (line)
		f.closed


if __name__ == "__main__":
    application.run()
