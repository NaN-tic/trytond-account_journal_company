# This file is part of the acount_journal_company module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, If
from trytond.transaction import Transaction

__all__ = ['Journal']


class Journal:
    __metaclass__ = PoolMeta
    __name__ = 'account.journal'
    company = fields.Many2One('company.company', 'Company', required=True,
        domain=[
            ('id', If(Eval('context', {}).contains('company'), '=', '!='),
                Eval('context', {}).get('company', -1)),
            ],
        select=True)

    @staticmethod
    def default_company():
        return Transaction().context.get('company')
