from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        num1 = 2
        num2 = 3
        end_num = 19
        res = solution(num1, num2, end_num)

        self.assertItemsEqual(res, [6, 12, 18])
