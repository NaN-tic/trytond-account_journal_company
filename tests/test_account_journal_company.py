# This file is part account_journal_company module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class AccountJournalCompanyTestCase(ModuleTestCase):
    'Test Account Journal Company module'
    module = 'account_journal_company'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AccountJournalCompanyTestCase))
    return suite
