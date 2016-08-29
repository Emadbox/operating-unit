# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "HR Contract Operating Unit",
    "version": "8.0.1.0.0",
    "license": 'AGPL-3',
    "author": "Eficent Business and IT Consulting Services S.L., "
              "Serpent Consulting Services Pvt. Ltd.,"
              "Odoo Community Association (OCA)",
    "website": "http://www.eficent.com",
    "category": "Generic Modules/Human Resources",
    "depends": ["hr_contract", "operating_unit"],
    "data": [
        "views/hr_contract_view.xml",
        "security/hr_contract_security.xml"
    ],
    'installable': True,
}
