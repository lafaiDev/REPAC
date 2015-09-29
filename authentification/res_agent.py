# import les bibiotique 
from openerp.osv import orm, fields
from openerp.tools.translate import _
class epac_agent(orm.Model):
    _inherit = 'res.users'
    _columns = {
        
        'note': fields.text('Note'),
		#'role': fields.selection([('agent','agent'),('Super','Super'),('chef','chef'),('admin,''admin')],'Role',required=True,readonly=True),
		'typecanalasterisk': fields.char('Type de canal Asterisk', size=64, required=True),
		'role': fields.selection([('agent','agent'),('Super','Super'),('chef','chef')],'Role'), 
		'ressource': fields.char('Nom de la ressource', size=64, required=True),
		'extension': fields.char('Extension', size=64, required=True),
		#relation
		#'equipe_ids':fields.many2one('epac.equipe','Equipe'),
		#'asterix_id': fields.many2one('epac.asterix','Asterix'),
		'equipe_ids':fields.many2many('epac.equipe','rel_equipe_agent','aid','eid','Equipe',ondelete='cascade'),
		'asterix_id':fields.many2many('epac.asterix','rel_agent_server','aid','sid','Server',ondelete='cascade'),
		'contact_id': fields.one2many('epac.contact','agent_id','Contact'),
		'trace_id': fields.one2many('epac.trace','agent_id','Trace'),
		
    }
    _default ={
    	'role':'agent',
    }
epac_agent()
	

