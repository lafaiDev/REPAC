# import les bibiotique 
from osv import fields,osv
class epac_qualification(osv.osv):
    _name = 'epac.qualification'
    _columns = {
        'idqualification': fields.char('IDqualification'),
        'name': fields.text('Name'),
        #relation
		'prospect_id': fields.one2many('epac.prospect','qualification_id','Prospect'),
    }
epac_qualification()