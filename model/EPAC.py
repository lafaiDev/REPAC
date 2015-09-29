# -*- coding: utf-8 -*-
##############################################################################
#
#	 OpenERP, Open Source Management Solution
#	 Copyright (C) 2014
#			by repac fatima & lafai
#
##############################################################################
# import les bibiotique 
from osv import fields,osv
from openerp import tools
import socket
import ftplib
import datetime
import time
import logging
import base64
_logger = logging.getLogger(__name__)

HOST="172.16.112.133"
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
	
class objet_enreg(osv.osv):
	_name = 'objet.enreg'
	_columns = {
		'name': fields.char('Name',size=64,required=True),
		'nomfichier': fields.char('nom de fichier', size=128),
		'extension': fields.char('extension'),
		'fichier': fields.binary('fichier', filters='*.wav'),
		'equipe_ids':fields.many2many('epac.equipe','rel_equipe_agent','aid','eid','Equipe',ondelete='cascade'),
		#relation
		#'contact_id': fields.many2one('epac.contact','Contact'),
		
		}
	def transfert_par_ftp(self, cr, uid, ids, context=None): 
		ftp=ftplib.FTP("172.16.112.133",'test','test')
		l=[]
		ftp.retrlines('LIST /var/spool/asterisk/monitor/', l.append) 
		for i in l:
			ftp.retrbinary('RETR /var/spool/asterisk/monitor/'+i.split()[8], open("." + i.split()[8], 'wb').write)
		ftp.quit()
   
objet_enreg()

class epac_contact(osv.osv):
	_name = 'epac.contact'
	
	_columns = {
		'idcontact': fields.char('idcontact'),
		'numcontact': fields.char('numcontact', size=128),
		'name': fields.char('Nom', size=128,required=True),
		'prenom': fields.char('Prenom', size=128),
		'telephone': fields.char('Telephone',size=9),
		'departement': fields.char('Departement', size=128),
		'email': fields.char('Email', size=128),
		'description': fields.text('Description'),
		'dateCreation': fields.date('DateCreation'),
		'dateModification': fields.date('DateModification'),
		'opportunite': fields.boolean('Opportunite'),
		'appelant': fields.text('appelant'),
		'fichier': fields.binary('fichier', filters='*.png,*.doc'),
		'nomfichier': fields.binary('nom du fichier', filters='*.png,*.doc'),
		#relation
		'prospect_ids': fields.many2one('epac.prospect','Prospect'),
		'etat_id': fields.many2one('epac.etat','Etat'),
		#'idobjetenreg': fields.one2many('objet.enreg','contact_id','Objetenreg'),
		'agent_id': fields.many2one('res.users','Agent'),
		'trace_id': fields.one2many('epac.trace','contact_id','Trace'),
	}
	def fcct(self, cr, uid, ids, context=None):
		data = self.browse(cr, uid, ids[0])							
		phone_to_dial = data.telephone
		#t=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
		self.pool.get('epac.appel').click_to_call(cr, uid, ids, phone_to_dial, username='user', password='secret', local_user='101', caller_id='101', wait_time='15', t=datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
		# le numero de lappele netant pas sur le formulaire, il sera recupere des infos dun user
		self.write(cr, uid, ids[0],{'appelant': '103'})
	
	def ftpfunction(self, cr, uid, ids, context=None):	
		return self.pool.get('epac.appel').transfert_par_ftttp(cr, uid, ids)
		
		
epac_contact()

class epac_prospect(osv.osv):
	_name = 'epac.prospect'
	_columns = {
		'iDprospect': fields.char('iDprospect', size=128),
		'name': fields.char('Nom', size=128,required=True),
		'telephone': fields.char('Telephone', size=9),
		'fax': fields.char('Fax', size=128),
		'boitePostale': fields.char('BoitePostale', size=128),
		'commentaire': fields.text('Commentaire'),
		'serin': fields.char('Serin', size=128),
		'siret': fields.char('Siret', size=128),
		'note': fields.text('Note'),
		'effectif': fields.char('Effectif', size=128),
		'statut': fields.char('Statut', size=128),
		'siteWeb': fields.char('SiteWeb', size=228),
		'secteur': fields.char('Secteur', size=128),
		'email': fields.char('Email', size=228),
		'origine': fields.char('Origine', size=128),
		'codePostal': fields.char('CodePostal', size=128),
		#Relation
        'contact_ids': fields.one2many('epac.contact','prospect_ids','Contact'),
        'type_id': fields.many2one('epac.type','Type'),
        'qualification_id': fields.many2one('epac.qualification','Qualification'),
		'adresse_id': fields.one2many('epac.adresse','prospect_id','Adresse'),
		'operateur_ids':fields.many2many('epac.operateur','rel_operateur_prospect','pid','oid','Operateur'),
		'compagne_id': fields.many2one('epac.compagne','Compagne'),
		'service_ids':fields.many2many('epac.service','rel_prospect_service','pid','sid','Service'),
		'appel_ids': fields.one2many('epac.appel','prospe_id','Appel pros'),

	}
	def fcct(self, cr, uid, ids, context=None):
		data = self.browse(cr, uid, ids[0])							
		phone_to_dial = data.telephone
		#t=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
		self.pool.get('epac.appel').click_to_call(cr, uid, ids, phone_to_dial, username='user', password='secret', local_user='101', caller_id='101', wait_time='15', t=datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
		# le numero de lappele netant pas sur le formulaire, il sera recupere des infos dun user
		self.write(cr, uid, ids[0],{'appelant': '102'})
		
epac_prospect()

class epac_appel(osv.osv):
	_name = 'epac.appel'
	_columns = {
		'description': fields.text('Description'),
		'chemin': fields.char('Chemin',size=128),
		'appelant': fields.char('appelant',size=128),
		'appele': fields.char('appel',size=128),
		'date': fields.char('date',size=128),
		'date_rappel': fields.date('date Rappele',size=128),
		'nomfichier': fields.char('nom de fichier', size=128),
		'extension': fields.char('extension'),
		'fichier': fields.binary('fichier', filters='*.png,*.doc'),
		
		#relation
		'trace_id': fields.many2one('epac.trace','Trace'),
		'prospe_id':fields.many2one('epac.prospect','Prospect'),
		}
	def verification(self, phone_to_dial):
		#vérifier si phone_to_dial: le numéro de lappelé nest pas vide (empty)
		if not phone_to_dial: 
			return False
		else:
			return True
	
	def transfert_par_ftttp(self, cr, uid, ids, context=None): 
		ftp=ftplib.FTP("172.16.112.133",'ahmed','ahmed')
		ids = self.search(cr, uid, [('fichier','=',False)]) 
		lines = self.browse(cr, uid, ids, context)
		
		for line in lines :
			_logger.info("appelant: " + line.appelant + ", appele: " + line.appele + ", date: " + line.date)
			#file_path = "C:\\Users\\faty\\Desktop\\enregestrement\\" + line.appelant + "-" + line.appele + "-" + line.date + ".wav"
			#localfile=open(file_path,'w+')
			file_path = "C:\\Users\\faty\\Desktop\\enregistrement\\" + line.appelant + "-" + line.appele + "-" + line.date + ".wav"
			localfile=open(file_path,'w+')
			ftp.retrbinary('RETR %s' % "/var/spool/asterisk/monitor/" + line.appelant + "-" + line.appele + "-" + line.date + ".wav", localfile.write)
			
			#ftp.retrbinary('RETR %s' % "/var/spool/asterisk/monitor/" + line.appelant + "-" + line.appele + "-" + line.date + ".wav", localfile.write)
			f = open(file_path, 'rb')
			#datas = f.read()
			datas_fname = line.appelant + "-" + line.appele + "-" + line.date + ".wav"
			#self.write(cr, uid, line.id, {'fichier': base64.b64encode(datas), 'nomfichier' : datas_fname})
			self.write(cr, uid, line.id, {'fichier': base64.b64encode(f.read()),'nomfichier' : datas_fname})
		ftp.quit()
		return True
		
	def click_to_call(self, cr, uid, ids, phone_to_dial, username, password, local_user, caller_id, wait_time, t):
		if self.verification(phone_to_dial):
			click_to_call2(phone_to_dial, username, password, local_user, caller_id, wait_time, t)
			_logger.info("dateeeeeeeeeeeee: " + t)
			self.create(cr, uid,{'appelant': local_user,'appele' : phone_to_dial,'date': t})
			_logger.info("dateeeeeeeeeeeee: " + t)
epac_appel()


class my_report_model(osv.osv):
	_name = "my.report.model"
	_description = "EPAC"
	_auto = False
	_columns = {
		'appelant': fields.char('appelant', size=128),
		'appele': fields.char('appele', size=9),
		'datee': fields.char('date appel', size=128),
		'fichier': fields.binary('enregistrement', filters='*.png,*.doc'),
		'nomfichier': fields.char('nom de fichier', size=128),
		'nom_contact': fields.char('nom contact', size=128),
		'nom_prospect': fields.char('nom prospect', size=128),
		
		}
	
	def init(self, cr):
		tools.sql.drop_view_if_exists(cr, 'my_report_model')
		cr.execute("""
				CREATE OR REPLACE VIEW my_report_model AS (
				SELECT	row_number() OVER () as id, crappel.appelant, crappel.appele, crappel.date AS datee, crappel.fichier, crcontact.name AS nom_contact, crprospect.name AS nom_prospect, crappel.nomfichier 
				FROM epac_appel crappel
				LEFT OUTER JOIN epac_contact crcontact ON crappel.appele = crcontact.telephone
				LEFT OUTER JOIN epac_prospect crprospect ON crappel.appele = crprospect.telephone)
		""")
	def ftpfun(self, cr, uid, ids, context=None):	
		return self.pool.get('epac.appel').transfert_par_ftttp(cr, uid, ids)
		
my_report_model()

class epac_report(osv.osv):
	_name = "epac.report"
	_description = "EPAC"
	_auto = False
	_columns = {
		'appelant': fields.char('appelant', size=128, readonly=True),
		'nombre': fields.integer('nombre dappels effectues', size=128, readonly=True),
		}
	
	def init(self, cr):
		tools.sql.drop_view_if_exists(cr, 'epac_report')
		cr.execute("""
				CREATE OR REPLACE VIEW epac_report AS (
				SELECT	row_number() OVER () as id, crappel.appelant, count(*) As nombre
				FROM epac_appel As crappel
				group by crappel.appelant)
		""")
epac_report()
