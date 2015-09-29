# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 meed (<http://www.meed.fr>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm, fields


class meedLog(orm.Model):
    _name = 'meed.log'
    _description = 'meed Logs'
    _rec_name = 'message'
    _log_access = False
    _order = 'log_date desc'

    def __init__(self, pool, cr):
        super(meedLog, self).__init__(pool, cr)
        cr.execute("select relname from pg_class where relname='meed_log'")
        if cr.rowcount:
            from db_handler import meedDBLogger
            logger = meedDBLogger(cr.dbname, '', 0, 0)
            logger.info('OpenERP server start')

    def _get_user_name(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        user_obj = self.pool.get('res.users')
        user_id_to_name = {}
        for log in self.browse(cr, uid, ids, context):
            if log.log_uid not in user_id_to_name:
                if user_obj.exists(cr, uid, log.log_uid, context):
                    name = user_obj.read(cr, uid, log.log_uid, ['name'], context)['name']
                    user_id_to_name[log.log_uid] = "%s [%s]" % (name, log.log_uid)
                else:
                    user_id_to_name[log.log_uid] = "[%s]" % (log.log_uid,)
            result[log.id] = user_id_to_name[log.log_uid]
        return result

    def _get_res_name(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        res_to_name = {}
        for log in self.browse(cr, uid, ids, context):
            res_key = (log.model_name, log.res_id)
            result[log.id] = "%s,%s" % res_key
            if log.model_name and log.res_id:
                if res_key in res_to_name:
                    result[log.id] = res_to_name[res_key]
                else:
                    if self.pool.get(log.model_name) and self.pool.get(log.model_name).exists(cr, uid, log.res_id, context):
                        name = self.pool.get(log.model_name).name_get(cr, uid, log.res_id, context)
                        if name and name[0]:
                            res_to_name[(log.model_name, log.res_id)] = name[0][1]
                            result[log.id] = name[0][1]
        return result

    _columns = {
        'log_date': fields.datetime('Date', readonly=True),
        'log_uid': fields.integer('User', readonly=True),
        'log_user_name': fields.function(_get_user_name, method=True, string='User', type='char', size=256),
        'log_res_name': fields.function(_get_res_name, method=True, string='Ressource name', type='char', size=256),

        'model_name': fields.char('Model name', size=64, readonly=True),
        'res_id': fields.integer('Ressource id', readonly=True, group_operator="count"),

        'pid': fields.integer('Pid', readonly=True, group_operator="count"),
        'level': fields.char('Level', size=16, readonly=True),
        'message': fields.text('Message', readonly=True),
    }

    def archive_and_delete_old_logs(self, cr, uid, nb_days=90, archive_path='', context=None):
        # Thanks to transaction isolation, the COPY and DELETE will find the same meed_log records
        if archive_path:
            file_name = time.strftime("%Y%m%d_%H%M%S.log.csv")
            file_path = os.path.join(archive_path, file_name)
            cr.execute(""" COPY (SELECT * FROM meed_log WHERE log_date + interval'%s days' < NOW())
            TO %s
            WITH (FORMAT csv, ENCODING utf8)""", (nb_days, file_path,))
        cr.execute("DELETE FROM meed_log WHERE log_date + interval '%s days' < NOW()", (nb_days,))
        return True
