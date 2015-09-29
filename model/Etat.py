# import les bibiotique 
from osv import fields,osv
class epac_etat(osv.osv):
    _name = 'epac.etat'
    _columns = {
        'idEtat': fields.char('idetat'),
        'name': fields.char('Etat contact'),
		'contact_id': fields.one2many('epac.contact','etat_id','Contact'),
    }
epac_etat()