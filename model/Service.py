# import les bibiotique 
from osv import fields,osv
class epac_service(osv.osv):
    _name = 'epac.service'
    _columns = {
        'idservice': fields.char('idService'),
        'name': fields.char('Name',size=128,required=True),
        'libelle': fields.text('Libelle'),
        #relation
		'operateur_ids':fields.many2many('epac.operateur','rel_operateur_service','sid','oid','Operateur'),
		'prospect_ids':fields.many2many('epac.prospect','rel_prospect_service','sid','pid','Prospect'),
    }
epac_service()