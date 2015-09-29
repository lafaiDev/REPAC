# import les bibiotique 
from osv import fields,osv
class epac_compagne(osv.osv):
    _name = 'epac.compagne'
    _columns = {
        'idCompagne': fields.char('IDCompagne'),
        'sujet': fields.text('Sujet'),
		'name': fields.char('Name',size=64,required=True),
		'datecreation': fields.date('Date Creation',required=True),
		'datefin': fields.date('Date Fin',required=True),
        'description': fields.text('Description'),
		
		#relation
		'equipe_id':fields.many2many('epac.equipe','res_compgne_equipe_rel', 'cid', 'eid','Equipe'),
		'client_id':fields.many2one('epac.client','Client'),
		'responsable_id': fields.many2one('res.users','Responsable'),
		'prospect_id': fields.one2many('epac.prospect','compagne_id','Prospect'),
    }
epac_compagne()