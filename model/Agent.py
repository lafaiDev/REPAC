# import les bibiotique 
from osv import fields,osv
class epac_agent(osv.osv):
    _name = 'epac.agent'
    _columns = {
        'idagent': fields.char('IDagent'),
        'note': fields.text('Note'),
		'typecanalasterisk': fields.char('Type de canal Asterisk', size=64, required=True),
		'ressource': fields.char('Nom de la ressource', size=64, required=True),
		'extension': fields.char('Extension', size=64, required=True),
		#relation
		#'equipe_ids':fields.many2one('epac.equipe','Equipe'),
		'asterix_id': fields.many2one('epac.asterix','Asterix'),
		'equipe_ids':fields.many2many('epac.equipe','rel_equipe_agent','aid','eid','Equipe',ondelete='cascade'),
		'contact_id': fields.one2many('epac.contact','agent_id','Contact'),
		'trace_id': fields.one2many('epac.trace','agent_id','Trace'),
    }
epac_agent()