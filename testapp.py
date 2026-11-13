import unittest
class TestApp(unittest.TestCase):
     def teat_addition(self):
       self.assertEqual(10+20,30)


if __name__=="__main__":
    unittest.main()