

import os, sys
import unittest

sys.path.append('../')
from datetime import date, datetime, timedelta
import SpindlerBattery, NubbinBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year-4)
        spindler = SpindlerBattery(today, last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_nubbin_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year-3)
        nubbin = NubbinBattery(today, last_service_date)
        self.assertFalse(nubbin.needs_service()) 

        nubbin.current_date = nubbin.current_date.replace(year=today.year+2)
        self.assertTrue(nubbin.needs_service())
 
        

class TestNubbinBattery(unittest.TestCase):
    def setUp(self):
        today = datetime.today().date()
        more_than_four_years_ago = today - timedelta(days=365*4+1)  
        less_than_four_years_ago = today - timedelta(days=365*4-1)  
        self.nubbin_that_needs_service = NubbinBattery(
            current_date=today,
            last_service_date=more_than_four_years_ago
        )
        self.nubbin_that_doesnt_need_service = NubbinBattery(
            current_date=today,
            last_service_date=less_than_four_years_ago
        )

    def test_should_need_service(self):
        self.assertTrue(
            self.nubbin_that_needs_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.nubbin_that_doesnt_need_service.needs_service()
        )

if __name__ == "__main__":
    unittest.main()