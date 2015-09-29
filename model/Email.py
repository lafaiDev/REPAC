# import les bibiotique 
from osv import fields,osv
class epac_email(osv.osv):
    _name = 'epac.email'
    _columns = {
		
		'type': fields.selection([
                        ('email', 'Email'),
                        ('comment', 'Comment'),
                        ('notification', 'System notification'),
                        ], 'Type',
            help="Message type: email for email message, notification for system "\
                 "message, comment for other messages such as user replies"),
        'objet': fields.char('Objet'),
		'date': fields.datetime('Date'),
		'corps': fields.html('Corps', help='Automatically sanitized HTML contents'),
        'description': fields.text('Description'),
        'destinataires': fields.text('Destinataires',help="Email address of the sender. This field is set when no matching partner is found for incoming emails."),
		'modele': fields.char('Utiliser un modele', size=128, select=1),
		'res_id': fields.integer('Related Document ID', select=1),
	#Relation
		#'subtype_id': fields.many2one('mail.message.subtype', 'Subtype',
         #   ondelete='set null', select=1,),
        'trace_id': fields.many2one('epac.trace','Trace'),
		'author_id': fields.many2one('res.partner', 'Author', select=1,
            ondelete='set null',
            help="Author of the message. If not set, email_from may hold an email address that did not match any partner."),
		#'parent_id': fields.many2one('epac.email', 'Parent Message', select=True,
         #   ondelete='set null', help="Initial thread message."),
 }
epac_email()