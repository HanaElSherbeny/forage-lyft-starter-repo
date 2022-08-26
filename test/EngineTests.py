
import unittest
import CapuletEngine
import WilloughbyEngine
import SternmanEngine

class TestCapuletEngine(unittest.TestCase):
    def setUp(self):
        self.capulet_that_needs_service = CapuletEngine(30_100, 0)
        self.capulet_that_doesnt_need_service = CapuletEngine(150, 50)

    def test_should_need_service(self):
        self.assertTrue(
            self.capulet_that_needs_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.capulet_that_doesnt_need_service.needs_service()
        )




class TestSternmanEngine(unittest.TestCase):
    def setUp(self):
        self.sternman_that_doesnt_need_service = SternmanEngine(warning_light_on=False)
        self.sternman_that_needs_service = SternmanEngine(warning_light_on=True)
        

    def test_should_need_service(self):
        self.assertTrue(
            self.sternman_that_needs_service.needs_service()
        )

    def test_should_not_need_service(self):
        self.assertFalse(
            self.sternman_that_doesnt_need_service.needs_service()
        )

if __name__ == "__main__":
    unittest.main()