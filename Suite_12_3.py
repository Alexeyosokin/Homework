import unittest
import tests_12_3

athleticsTS = unittest.TestSuite()
athleticsTS.addTest(unittest.TestLoader() \
                    .loadTestsFromTestCase(tests_12_3.RunnerTest))
athleticsTS.addTest(unittest.TestLoader() \
                    .loadTestsFromTestCase(tests_12_3.TournamentTest))
ut_runner = unittest.TextTestRunner(verbosity=2)
ut_runner.run(athleticsTS)