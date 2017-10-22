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
import comm
import julius

######################################
#  Julius Server
#
def main(num=10000, top="html", host="", ssl=False):
  if type(num) == str: num = int(num)
  reader = comm.HttpReader(None, top)
  reader.asr = julius.JuliusWrap()
  reader.asr.startJulius()
  reader.asr.start()

  srv=comm.SocketServer(reader, "JuliusServer", host, num, ssl)
  srv.start()
  return srv

