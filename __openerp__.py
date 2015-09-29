##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014  BY EPAC
##########################################

#	contient toutes les information sur notre module
{
#												les ddonner sous forme (cle:value) separer par une virgule  
        "name" : "REPAC",						#le nom du module
        "version" : "0.3",						#la version du module
        "author" : "lafai",						#l'auteur de du module
        "website" : "ahmed.lafai@edu.uiz.ac.ma",		
        "category" : "CRM-appel-emal-prospection-coptable-facturation",				#la categorie dans laquelle classez mon module
        "description": """  """,				#description de module  ("""èè""" pour inser un text sur # ligne)
        "depends" : ['base'],					#les module depende de mon module
        "init_xml" : [ ],
        "demo_xml" : [ ],
        "update_xml" : [
						
						'security/epac_security.xml',
						'menu_repac.xml',
						'security/ir.model.access.csv',
					#	'security/ir.model.access.csv',
					#	'security/epac_security.xml',
				#		'security/epac_security.xml',
				#		'security/ir.model.accessadmin.csv',
				#		'security/ir.model.accessagent.csv',
				#		'security/ir.model.accesssuper.csv',
				#		'security/ir.model.accesschef.csv',
						'view/board_view.xml',
				#		'view/board_mydashboard_view.xml',
						'journale/trace_log_view.xml',
						'view/equipe_view.xml',
                        'view/adress_view.xml',
                        'view/appel_view.xml',
                        'view/client_view.xml',
                        'view/compagne_view.xml',
                        'view/contact_view.xml',
                        'view/email_view.xml',
                        'view/etat_view.xml',
                        'view/meeting_view.xml',
                        'view/operateur_view.xml',
                        'view/prospect_view.xml',
						'view/qualification_view.xml',
                        'view/asterix_view.xml',
						'view/service_view.xml',
                        'view/type_view.xml',
						
                    #   	    'view/chef_compagne_view.xml', 
                    # 	 		'view/superviseur_view.xml',
					# 			'view/agent_view.xml',
					#			'data/res_user_data.xml',
					#    	    'authentification/res_group_view.xml',
					#			'authentification/res_user_view.xml',
						'authentification/res_super_view.xml',
						'authentification/res_chef_view.xml',
						'authentification/res_agent_view.xml',
						'view/EPAC_view.xml',
						
                        ],
		"js": ['static/src/js/dashboard.js'],
		"css": ['static/src/css/dashboard.css'],
		"qweb": ['static/src/xml/*.xml'],
        "installable": True,
		"auto_install": False,
		"images": ['images/1_dashboard_definition.jpeg','images/2_publish_note.jpeg','images/3_admin_dashboard.jpeg',],
}
