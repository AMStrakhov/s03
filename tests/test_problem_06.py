from typing import Callable, List, Tuple

from problem_06 import main
from .base_test_problem import BaseTestProblem


class TestProblem06(BaseTestProblem):
    _problem_func: Callable = main
    cases: List[Tuple[List, str, str]] = [
        (["12", "8"], "4", "12 & 8"),
        (["20", "8"], "4", "20 & 8"),
        (["0", "1"], "1", "0 & 1"),
        (["12", "12"], "12", "12 & 12"),
    ]
    modules_to_patch = ["math.gcd", "problem_01.gcd"]

    def test_problem(self) -> None:
        self._test_problem()
