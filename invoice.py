# This file is part of the acount_journal_company module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Invoice']


class Invoice:
    __metaclass__ = PoolMeta
    __name__ = 'account.invoice'

    @classmethod
    def __setup__(cls):
        super(Invoice, cls).__setup__()
        journal_domain = ('company', '=', Eval('company', -1))
        journal_depends = ['company']
        if cls.journal.domain:
            cls.journal.append(journal_domain)
        else:
            cls.journal = journal_domain
        if cls.journal.depends:
            cls.journal.depends += journal_depends
        else:
            cls.journal.depends = journal_depends
