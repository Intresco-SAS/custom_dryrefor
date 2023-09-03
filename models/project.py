# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ProjectTask(models.Model):

    _inherit = ["project.task"]

    es_pagado = fields.Selection([('inpagado', 'Sin Pagar'),
                                  ('pagado', 'Pagado')], 
                                  string='Pagado')

    cancelation_note = fields.Char("Motivo de la cancelacion")

    def cancelar_tarea_wiz(self):
        task_cancel_form = self.env.ref('custom_dryrefor.project_task_cancel_wizard_view', False)
        return {
            'name': 'Wizard cancel task',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'project.task.cancel',
            'views': [(task_cancel_form.id, 'form')],
            'view_id': task_cancel_form.id,
            'target': 'new',
            'context': {}
        }

    def action_toggle_paid(self):
        if self.es_pagado == 'pagado':
            self.es_pagado = 'inpagado'
        else:
            self.es_pagado = 'pagado'
