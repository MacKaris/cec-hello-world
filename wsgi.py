import socket
import time
import os.path
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():    
	print ("spede")
	#return "Hello Wooiorld! Greetings from "+socket.gethostname()+"\n"
	#return "Rock rock! \n"    

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
		result = []
		for line in f:
			result.append(line)
	f.closed
	return result

if __name__ == "__main__":
	application.run()
