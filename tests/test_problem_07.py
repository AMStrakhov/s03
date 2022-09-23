from typing import Callable, List, Tuple

from problem_07 import main
from .base_test_problem import BaseTestProblem


class TestProblem07(BaseTestProblem):
    _problem_func: Callable = main
    cases: List[Tuple[List, str, str]] = [
        (["0"], "", "0"),
        (["1"], "0", "1"),
        (
            ["10"],
            (
                "0 A 2 3 4 5 6 7 8 9\n"
                "0 A 2 3 4 5 6 7 8 9\n"
                "0 A 2 3 4 5 6 7 8 9\n"
                "0 A 2 3 4 5 6 7 8 9\n"
                "0 A 2 3 4 5 6 7 8 9\n"
                "0 A 2 3 4 5 6 7 8 9\n"
                "0 A 2 3 4 5 6 7 8 9\n"
                "0 A 2 3 4 5 6 7 8 9\n"
                "< O > > > > > > > >\n"
                "0 V 2 3 4 5 6 7 8 9"
            ),
            "10",
        ),
        (
            ["5"],
            "0 A 2 3 4\n0 A 2 3 4\n0 A 2 3 4\n< O > > >\n0 V 2 3 4",
            "5",
        ),
    ]

    def test_problem(self) -> None:
        self._test_problem()
