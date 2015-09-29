# import les bibiotique 
from osv import fields,osv
class epac_prospect(osv.osv):
    _name = 'epac.prospect'
    _columns = {
		'idprospect': fields.char('iDprospect', size=128),
		'nom': fields.char('Nom', size=128,required=True),
		'telephone': fields.char('Telephone', size=128),
		'fax': fields.char('Fax', size=128),
		'boitePostale': fields.char('BoitePostale', size=128),
		'commentaire': fields.char('Commentaire', size=228),
		'serin': fields.char('Serin', size=128),
		'siret': fields.char('Siret', size=128),
		'note': fields.text('Note'),
		'effectif': fields.char('Effectif', size=128),
		'statut': fields.char('Statut', size=128),
		'siteWeb': fields.char('SiteWeb', size=228),
		'secteur': fields.char('Secteur', size=128),
		'email': fields.char('Email', size=228),
		'origine': fields.char('Origine', size=128),
		'codePostal': fields.char('CodePostal', size=128),
		'pros_email': fields.related('email', type='char',
            deprecated='Use the email field instead of user_email. This field will be removed with OpenERP 7.1.'),
		#Relation
		'contact_ids': fields.one2many('epac.contact','prospect_ids','Contact'),
        'type_id': fields.many2one('epac.type','Type'),
        'qualification_id': fields.many2one('epac.qualification','Qualification'),
		'adresse_id': fields.one2many('epac.adresse','prospect_id','Adresse'),
		'operateur_ids':fields.many2many('epac.operateur','rel_operateur_prospect','pid','oid','Operateur'),
		'compagne_id': fields.many2one('epac.compagne','Compagne'),
		'service_ids':fields.many2many('epac.service','rel_prospect_service','pid','sid','Service'),
    }
    def send_email(self, cr, uid, ids, context=None):
        return {
            'type': 'ir.actions.client',
            'tag': 'send_mail',
            'target': 'new',
    }
    #def send_mail(self, cr, uid, context=None):
    #    """
    #    """
        #self.check(cr.dbname, uid, old_passwd)
        #if new_passwd:
            #return self.write(cr, uid, uid, {'password': new_passwd})
        #raise osv.except_osv(_('Warning!'), _("Setting empty passwords is not allowed for security reasons!"))
epac_prospect()