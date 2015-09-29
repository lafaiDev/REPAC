# import les bibiotique 
from osv import fields,osv
class epac_chefcompagne(osv.osv):
    _name = 'epac.chefcompagne'
    _columns = {
        'idChef': fields.char('idchef'),
		#relation
		'idcompagne': fields.one2many('epac.compagne','responsable_id','Compagne'),
		
    }
epac_chefcompagne()