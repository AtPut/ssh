from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_A1_is_1(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1")
        self.assertEqual(1, spreadsheet.get("A1"))

    def test_A1_is_Error_when_decimal_number(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1.5")
        self.assertEqual("#Error", spreadsheet.get("A1"))

    def test_if_string_contains_only_one_quote_mark_is_Error(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple")
        self.assertEqual("#Error", spreadsheet.get("A1"))

    def test_if_formula_string_contains_only_one_quote_mark_is_Error(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple")
        self.assertEqual("#Error", spreadsheet.get("A1"))

    def test_Formula_in_A1_is_1_when_decimal(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1")
        self.assertEqual(1, spreadsheet.get("A1"))

    def test_if_formula_string_contains_two_quote_mark_is_Apple(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("'Apple'", spreadsheet.get("A1"))

