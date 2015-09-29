# import les bibiotique 
from osv import fields,osv
class epac_trace(osv.osv):
    _name = 'epac.trace'
    _columns = {
        'idTrace': fields.char('idtrace'),
		'name': fields.char('Name',size=64),

        #relation
        'meeting_id':fields.many2one('epac.meeting','Meeting'),
        'agent_id': fields.many2one('epac.agent','Agent'),
        'contact_id': fields.many2one('epac.contact','Contact'),
        'appel_id': fields.one2many('epac.appel','trace_id','Appel'),
        'email_id': fields.one2many('epac.email', 'trace_id','Email'),
    }
epac_trace()