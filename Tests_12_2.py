import unittest
import inspect
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({k: str(v) for k, v in cls.all_results[test].items()})

    def test_usain_nik(self):
        tour = Tournament(90, self.usain, self.nik)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_andrey_nik(self):
        tour = Tournament(90, self.andrey, self.nik)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_usain_andrey_nik(self):
        tour = Tournament(90, self.usain, self.andrey, self.nik)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_nik_andrey_usain_8(self):
        tour = Tournament(8, self.nik, self.andrey, self.usain)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)


if __name__ == '__main__':
    unittest.main()


'''
.F..

test_andrey_nik:
{1: 'Андрей', 2: 'Ник'}

test_nik_andrey_usain_8:
{1: 'Андрей', 2: 'Ник', 3: 'Усэйн'}

test_usain_andrey_nik:
{1: 'Усэйн', 2: 'Андрей', 3: 'Ник'}

test_usain_nik:
{1: 'Усэйн', 2: 'Ник'}

======================================================================
FAIL: test_nik_andrey_usain_8 (__main__.TournamentTest.test_nik_andrey_usain_8)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests_12_2.py", line 46, in test_nik_andrey_usain_8
    self.assertTrue('Ник' == results[len(results)].name)
AssertionError: False is not true

----------------------------------------------------------------------
Ran 4 tests in 0.006s

FAILED (failures=1)




Возможно, ошибка проявляется, когда дистанция турнира одного порядка со
скоростью бегуна. Её можно избежать, если ввести параметр отрезка времени, за
который вычисляется дистанция (период дискретизации) и выставить его значение
в 10 раз меньше отношения дистанции к скорости.

class Runner:
    ...
    def run(self, sampling_interval=1):
        self.distance += sampling_interval * self.speed * 2

    def walk(self, sampling_interval=1):
        self.distance += sampling_interval * self.speed
    ...

class Tournament:
    ...
    def start(self, sampling_interval=1):
                ...
                participant.run(sampling_interval)
                ...

class TournamentTest(unittest.TestCase):
    ...
    def test_nik_andrey_usain_8(self):
        ...
        results = tour.start(0.1)
        ...
'''