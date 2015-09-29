# import les bibiotique 
from osv import fields,osv
class epac_superviseur(osv.osv):
    _name = 'epac.superviseur'
	
    _columns = {
        
		'idsuperviseur': fields.integer('ID'),
		'note':fields.text("Note"),
  }
		   
epac_superviseur()