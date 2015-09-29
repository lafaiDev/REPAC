# import les bibiotique 
from osv import fields,osv
class epac_adresse(osv.osv):
    _name = 'epac.adresse'
    _columns = {
        'name': fields.char('Name'),
		'commentaire': fields.text('Commentaire'),
        'avenue': fields.char('Avenue'),
        'boitePostale': fields.integer('BoitePostale'),
        'codePostal': fields.integer('CodePostal'),
        'ville': fields.char('Ville'),
        'pays': fields.char('Pays'),

		'prospect_id':fields.many2one('epac.prospect','Prospect'),
    }
epac_adresse()