# import les bibiotique 
from openerp.osv import orm, fields
from openerp.tools.translate import _
from openerp import tools
import socket
import ftplib
import datetime
import time
import logging
import base64
_logger = logging.getLogger(__name__)

HOST="192.168.129.213"
PORT=5038

a = """Action: login
Events: off
Username: %(username)s
Secret: %(password)s
 
"""
 
b = """Action: originate
Channel: SIP/%(local_user)s
WaitTime: %(wait_time)s
CallerId: %(caller_id)s
Exten: %(phone_to_dial)s
Context: default
Priority: 1

"""

c = """Action: Command
Command: core show channels

"""
d = """Action: Monitor
Channel: %(cannal)s
File: %(local_user)s-%(phone_to_dial)s-%(temps)s
Mix: true

"""

e = """Action: Logoff

"""

def click_to_call2(phone_to_dial, username, password, local_user, caller_id, wait_time, t): 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	data = s.recv(1024)
	_logger.info("connexion socket" + data + "fin connexion socket")
	
	pattern0 = a % {
		'username': username,
		'password': password}
	for l in pattern0.split('\n'):
		_logger.info("Sending>" + l)
		s.send(l+'\r\n')
		if l == "":
			data = s.recv(1024)
			_logger.info("apres login 1: " + data + "fin login 1")
	data = s.recv(1024)
	_logger.info("apres login 2: " + data + "fin login 2")
	
	pattern1 = b % {
		'phone_to_dial': phone_to_dial,
		'username': username,
		'password': password,
		'local_user': local_user,
		'caller_id': caller_id,
		'wait_time': wait_time}
	for l in pattern1.split('\n'):
		_logger.info("Sending>" + l)
		s.send(l+'\r\n')
		if l == "":
			data = s.recv(1024)
			_logger.info("apres originate 1: " + data + "fin originate")
	data = s.recv(1024)
	_logger.info("apres originate 2: " + data + "fin originate 2")
	
	for l in c.split('\n'):
		_logger.info("Sending>" + l)
		s.send(l+'\r\n')
		if l == "":
			data = s.recv(1024)
			_logger.info("apres command 1: " + data + "fin command 1")
	data = s.recv(1024)
	_logger.info("apres command 2: " + data + "fin command 2")
	can=data[data.find("SIP"):(data.find("SIP"))+16]
	_logger.info("canal : " + can + "fin")
	
	pattern3 = d % {  
		'phone_to_dial': phone_to_dial,
		'local_user': local_user,
		'temps': t,
		'cannal': can}
	for l in pattern3.split('\n'):
		_logger.info("Sending>" + l)
		s.send(l+'\r\n')
		if l == "":
			data = s.recv(1024)
			_logger.info("apres monitor 1: " + data + "fin monitor1")
	data = s.recv(1024)
	_logger.info("apres monitor 2: " + data + "fin monitor2")
	
	for l in e.split('\n'):
		_logger.info("Sending>" + l)
		s.send(l+'\r\n')
		if l == "":
			data = s.recv(1024)
			_logger.info("apres logoff 1: " + data + "fin logoff 1")
	data = s.recv(1024)
	_logger.info("apres logoff 2: " + data + "fin logoff2")
	
	s.close()
			
class epac_appel(orm.Model):
	_name = 'epac.appel'
	
	_columns = {
		'description': fields.text('Description'),
		'chemin': fields.char('Chemin',size=128),
		'appelant': fields.char('appelant',size=128),
		'appele': fields.char('appel',size=128),
		'date': fields.char('date',size=128),
		'nomfichier': fields.char('nom de fichier', size=128),
		'extension': fields.char('extension'),
		'fichier': fields.binary('fichier', filters='*.png,*.doc'),
	   #relation
		'trace_id': fields.many2one('epac.trace','Trace'),
	}
