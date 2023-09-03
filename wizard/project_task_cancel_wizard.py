# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProjectTaskCancel(models.TransientModel):

    _name = 'project.task.cancel'

    cancelation_note = fields.Char("Motivo de la cancelacion", required=1)

    #@api.multi
    def cancelar_tarea(self):
        tarea = self.env['project.task'].browse(self._context.get('active_id'))
        tarea.cancelation_note = self.cancelation_note
        tarea.active = False
        tarea.message_post(body=('Tarea Archivada'))
        return True
