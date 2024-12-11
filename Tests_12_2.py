import random


class TestCase:
    def __init__(self, name):
        self.case_id = random.randrange(100, 1000)
        self.name = name
        self.steps = {}
        self.result = None

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        del self.steps[step_number]

    def get_steps(self):
        return self.steps

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        print({'id': self.case_id, 'Название': self.name, 'Шаги': self.steps, 'Ожидаемый результат': self.result})
