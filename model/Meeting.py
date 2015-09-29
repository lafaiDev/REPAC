# import les bibiotique 
from osv import fields,osv
class epac_meeting(osv.osv):
    _name = 'epac.meeting'
    _columns = {
		'name': fields.char('Name',size=64,required=True),
        'idRDV': fields.char('IdRDV'),
        'dateRDV': fields.datetime('DateRDV'),
        'description': fields.text('Description'),
		'trace_id': fields.one2many('epac.trace','meeting_id','Trace'),
    }
epac_meeting()