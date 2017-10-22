# -*- coding: utf-8 -*-
#
#  PyWebScok Library
#  Communication Adaptor for WebSocket
#
#   Copyright(C) 2015, Isao Hara, AIST, All Right Reserved
#   Licensed under the MIT License.
#   http://www.opensource.org/licenses/MIT
#

################################
import sys
import signal
import comm
import julius
from daemonize import Daemonize

global __srv

def signalHandler(sig, handler):
   global __srv
   print "Call sig"

   if __srv :
     __srv.terminate()
   else:
     print "No service found"
   sys.exit()

######################################
#  Julius Server
#
def main(num=10000, top="html", host="", ssl=False, make_thread=True):
  global __srv
  if type(num) == str: num = int(num)
  reader = comm.HttpReader(None, top)
  reader.asr = julius.JuliusWrap()
  reader.asr.startJulius()
  reader.asr.start()

  __srv=comm.SocketServer(reader, "JuliusServer", host, num, ssl)
  signal.signal(signal.SIGINT,  signalHandler)
  if make_thread :
    __srv.start()
  else:
    __srv.main_loop() 

  return __srv

def main2(num=10000):
  main(num=num, make_thread=False)

#
#
if __name__ == '__main__' :
  __srv=main2()
  #dmn = Daemonize(app="Julius", pid='/tmp/julius.pid', action=main2)
  #dmn.start() 
  
  
