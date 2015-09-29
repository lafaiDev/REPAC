# import les bibiotique 
from osv import fields,osv
class epac_type(osv.osv):
    _name = 'epac.type'
    _columns = {
        'idtype': fields.char('IDType'),
        'name': fields.text('Name'),
		'prospect_id': fields.one2many('epac.prospect','type_id','Prospect'),
    }
epac_type()