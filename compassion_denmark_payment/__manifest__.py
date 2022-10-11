# Copyright 2013-2020 Akretion (www.akretion.com)
# Copyright 2014-2020 Tecnativa - Pedro M. Baeza & Antonio Espinosa
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Compassion Denmark Payment",
    "summary": "Create Denmark Direct Debit",
    "version": "14.0.1.3.3",
    "license": "AGPL-3",
    "category": "Banking addons",
    "depends": ["account_banking_pain_base", "account_banking_mandate", "compassion_mandate_upload",
                "account_statement_import", "recurring_contract", "sponsorship_compassion"],
    "data": [
        "data/account_payment_method.xml",
    ],
    "installable": True,
}