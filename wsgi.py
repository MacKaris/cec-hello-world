import socket
import time
import os.path
from flask import Flask

application = Flask(__name__)

@application.route("/")

print("on tamakin saatana tyomaa")
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
		for line in f:
			print (line)
		f.closed

if __name__ == "__main__":
	application.run()
