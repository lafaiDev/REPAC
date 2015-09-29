# import les bibiotique 
from osv import fields,osv
class epac_contact(osv.osv):
    _name = 'epac.contact'
    _columns = {
		'idcontact': fields.char('idcontact'),
		'numcontact': fields.char('numcontact', size=128),
		'nom': fields.char('Nom', size=128,required=True),
		'prenom': fields.char('Prenom', size=128),
		'telephone': fields.char('Telephone', size=128,required=True),
		'departement': fields.char('Departement', size=128),
		'description': fields.text('Description'),
		'dateCreation': fields.date('DateCreation'),
		'dateModification': fields.date('DateModification'),
        'opportunite': fields.boolean('Opportunite'),
		#relation
		'prospect_ids': fields.many2one('epac.prospect','Prospect'),
		'etat_id': fields.many2one('epac.etat','Etat'),
		'agent_id': fields.many2one('res.users','Agent'),
		'trace_id': fields.one2many('epac.trace','contact_id','Trace'),
    }
		
epac_contact()