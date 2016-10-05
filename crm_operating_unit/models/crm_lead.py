# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from openerp import api, fields, models, _
from openerp.exceptions import UserError


class CRMLead(models.Model):

    _inherit = 'crm.lead'

    @api.model
    def _get_default_operating_unit(self):
        if 'default_team_id' in self.env.context:
            team_id = self.env.context['default_team_id']
            team = self.env['crm.team'].browse(team_id)
            return team.operating_unit_id
        else:
            return self.env['res.users'].operating_unit_default_get(self._uid)

    operating_unit_id = fields.Many2one('operating.unit', 'Operating Unit',
                                        default=_get_default_operating_unit)

    @api.onchange('team_id')
    def onchange_team_id(self):
        self.operating_unit_id = self.team_id.operating_unit_id

    @api.multi
    @api.constrains('team_id', 'operating_unit_id')
    def _check_team_operating_unit(self):
        for rec in self:
            if (rec.team_id and rec.operating_unit_id and
                    rec.team_id.operating_unit_id != rec.operating_unit_id):
                raise UserError(_('Configuration error!\nThe Company in the'
                                  ' Move Line and in the Operating Unit must '
                                  'be the same.'))
