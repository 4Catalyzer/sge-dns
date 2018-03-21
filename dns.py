import logging
import socket
import time

from dnslib.server import DNSServer, DNSLogger
from dnslib import RR, QTYPE

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

class TestResolver:
    def resolve(self,request,handler):
        qname = request.q.qname
        qtype = 'A'#QTYPE[request.q.qtype]
        ip = socket.gethostbyname(qname.label[0])
        reply = request.reply()
        reply.add_answer(*RR.fromZone("%s 180 %s %s" % (qname, qtype, ip)))
        return reply

logger_dns = DNSLogger()

resolver = TestResolver()

server_udp = DNSServer(resolver, port=53, address="", logger=logger_dns)
server_udp.start_thread()

server_tcp = DNSServer(resolver, port=53, address="", logger=logger_dns, tcp=True)
server_tcp.start_thread()

while server_udp.isAlive():
    time.sleep(1)
