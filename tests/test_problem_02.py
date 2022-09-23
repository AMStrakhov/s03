from typing import Callable, List, Tuple

from problem_02 import main
from .base_test_problem import BaseTestProblem


class TestProblem02(BaseTestProblem):
    _problem_func: Callable = main
    cases: List[Tuple[List, str, str]] = [
        (["10", "3"], "0\n3\n6\n9", "Base case"),
        (["-10", "3"], "0\n-3\n-6\n-9", "Negative limit"),
        (["10", "0"], "Error: Division by zero", "Divider is 0"),
        (["10", "-3"], "0\n3\n6\n9", "Negative divider"),
        (["3", "6"], "0", "Divider exceeds limit"),
        (["0", "3"], "0", "Limit is 0"),
        (["10", "5"], "0\n5\n10", "Biggest divider == limit"),
    ]

    def test_problem(self) -> None:
        self._test_problem()
