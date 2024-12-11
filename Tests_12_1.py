import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner('Alex')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        run = runner.Runner('Miron')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        walker2 = runner.Runner('Mila')
        run2 = runner.Runner('Sofia')
        for i in range(10):
            walker2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walker2.distance)

