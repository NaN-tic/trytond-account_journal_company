# This file is part account_journal_company module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import account
from . import invoice


def register():
    Pool.register(
        account.Journal,
        invoice.Invoice,
        module='account_journal_company', type_='model')
