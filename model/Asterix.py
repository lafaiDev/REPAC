# import les bibiotique 
from osv import fields,osv
class epac_asterix(osv.osv):
    _name = 'epac.asterix'
	
    _columns = {
        		      
        'name': fields.char('Nom Serveur', size=128, required=True),
		'active': fields.boolean('Active'), 
		'adresseIP': fields.char('Adresse IP', size=30, required=True),
        'port': fields.char('Port', size=15, required=True),
        'userAMI': fields.char('User AMI', size=64, required=True),
        'passwdAMI': fields.char('Password AMI', size=64, required=True),
		'contextdialplan': fields.char('Context du dialplan', size=64, required=True),
		'note': fields.text('Note'),
		
		#relation
		#'idagent': fields.one2many('res.users','asterix_id','Agent'),
		'agent_id':fields.many2many('res.users','rel_agent_server','sid','aid','User'),
		
		}
epac_asterix()