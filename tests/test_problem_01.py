from typing import Callable, List, Tuple

from problem_01 import main
from .base_test_problem import BaseTestProblem


class TestProblem01(BaseTestProblem):
    _problem_func: Callable = main
    cases: List[Tuple[List, str, str]] = [
        (["0"], "", "0"),
        (["1"], "0", "1"),
        (
            ["10"],
            (
                "0 1 2 3 4 5 6 7 8 9\n"
                "0 1 2 3 4 5 6 7 8 9\n"
                "0 1 2 3 4 5 6 7 8 9\n"
                "0 1 2 3 4 5 6 7 8 9\n"
                "0 1 2 3 4 5 6 7 8 9\n"
                "0 1 2 3 4 5 6 7 8 9\n"
                "0 1 2 3 4 5 6 7 8 9\n"
                "0 1 2 3 4 5 6 7 8 9\n"
                "0 1 2 3 4 5 6 7 8 9\n"
                "0 1 2 3 4 5 6 7 8 9"
            ),
            "10",
        ),
        (
            ["5"],
            "0 1 2 3 4\n0 1 2 3 4\n0 1 2 3 4\n0 1 2 3 4\n0 1 2 3 4",
            "5",
        ),
    ]

    def test_problem(self) -> None:
        self._test_problem()
