# -*- encoding: utf-8 -*-


from openerp.osv import orm, fields
from openerp.tools.translate import _


class ResSuper(orm.Model):
    _inherit = 'res.users'

    _columns = {
	#'role': fields.selection([('Agent','Agent'),('Super','Super')],'Role',readonly=True), 
        'test': fields.char('Test'),
		
		'idequipe': fields.one2many('epac.equipe','superviseur_id','Superviseur'),
    }
    default={
    	'role':'Super',
    }
   