#
# DLT Server
#
import os
import sys
import zmq
import time

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, BASE_PATH + '/lib')
import dlt

def main(args):
    # Initialize the DLT tester
    tester = dlt.DrupalLoadTest()
    
    # Get config parser
    config = tester.config.get()
    
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:" + config['Server']['port'])
    
    while True:
        #  Wait for next request from client
        message = socket.recv()
        print "Received request: ", message

        #  Do some 'work'
        time.sleep (1)

        #  Send reply back to client
        socket.send("World")
        
    
if __name__ == "__main__":
  try:
      main(sys.argv[1:])
  except KeyboardInterrupt:
      dlt.log("Interrupted by input. Exiting.")