# import les bibiotique 
from osv import fields,osv
class epac_operateur(osv.osv):
    _name = 'epac.operateur'
    _columns = {
        'idoperateur': fields.char('idOperateur'),
        'name': fields.char('Name',size=128,required=True),
		'prospect_ids':fields.many2many('epac.prospect','rel_operateur_prospect','oid','pid','Prospect'),
		'service_ids':fields.many2many('epac.service','rel_operateur_service','oid','sid','Service'),
    }
epac_operateur()