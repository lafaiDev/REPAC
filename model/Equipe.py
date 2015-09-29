# import les bibiotique 
from openerp.osv import orm, fields
from openerp.tools.translate import _

class epac_equipe(orm.Model):	    #cree un objet epac_equipe
    """(NULL)"""
    _name = 'epac.equipe'			#nom de la table dans openERP 
									#(le vrais nom dans la basse de donner et epac_equipe)
    _columns = {					#les champs que l'on cree 
									#dans la table epac_equipe
        
        'name': fields.char('Equipe de projet', size=64, required=True, translate=True),
        'datecree': fields.date('datecree',required=True),
		'code': fields.char('Code', size=8),
        'active': fields.boolean('Active', help="If the active field is set to "\
                        "true, it will allow you to hide the sales team without removing it."),
	    'note': fields.text('Note'),
		#relation 
		#'user_id': fields.many2one('res.users', 'superviseur'),
		'superviseur_id': fields.many2one('res.users', 'Superviseur'),
		'compagne_id': fields.many2many('epac.compagne','rel_compgne_equipe', 'eid', 'cid','Compagne',ondelete='cascade'),
		'agent_ids': fields.many2many('res.users','rel_equipe_agent','eid','aid','Agent'),
		
		
		#'resource_calendar_id': fields.many2one('resource.calendar', "Working Time", help="Used to compute open days"),
        
    }
    _sql_constraints = [
		('uniq_name', 'unique(name, compagne_id)', "Equipe already exists with this name in this compagne. Equipe name must be unique!"),
	]
    #def init(self, cr):
	#	tools.sql.drop_view_if_exists(cr, 'epac_equipe')
	#	cr.execute("""
	#			CREATE OR REPLACE VIEW epac_equipe AS (
	#			SELECT	row_number() OVER () as id, *
	#			FROM epac_compagne As compagne
	#			LEFT OUTER JOIN epac_equipe  ON crappel.appele = crcontact.numcontact 
	#			LEFT OUTER JOIN epac_prospect crprospect ON crappel.appele = crprospect.telephone)
	#	""")
#epac_equipe()