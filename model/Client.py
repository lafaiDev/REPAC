# import les bibiotique 
from osv import fields,osv
class epac_client(osv.osv):
    _name = 'epac.client'
    _columns = {
        'idclient': fields.char('IDClient'),
		'name': fields.char('Name', size=128, required=True, select=True),
		'email': fields.char('Email', size=240),
        'phone': fields.char('Telephone', size=64),
        'fax': fields.char('Fax', size=64),
        'mobile': fields.char('Mobile', size=64),
        'libelle': fields.char('Libelle'),
        'note': fields.text('Note'),
		#relation
        'compagne_ids': fields.one2many('epac.compagne','client_id','Compagne',required=True),
		}
epac_client()