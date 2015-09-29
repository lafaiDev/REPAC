# -*- encoding: utf-8 -*-


from openerp.osv import orm, fields
from openerp.tools.translate import _


class Res_chef_compagne(orm.Model):
    _inherit = 'res.users'
	
    _columns = {
		'idChef': fields.char('idchef'),
		'note': fields.text('Note'),
		'dateajout': fields.date('date ajout',required=True),
	#relation
		'idcompagne': fields.one2many('epac.compagne','responsable_id',groups='base.group_repac_chefprojet,base.group_repac_admin'),
    }
    default={
    	'role':'chef',
    }
   