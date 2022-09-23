from typing import Callable, List, Tuple

from problem_05 import main
from .base_test_problem import BaseTestProblem


class TestProblem05(BaseTestProblem):
    _problem_func: Callable = main
    cases: List[Tuple[List, str, str]] = [
        (["0"], "OK\nFinished", "Zero"),
        (["1"], "OK\nFinished", "Integer"),
        (["-1"], "OK\nFinished", "Negative Integer"),
        (
            ["1.2345"],
            "Error: invalid literal for int() with base 10: '1.2345'\nFinished",
            "Float",
        ),
        (
            ["-1.2345"],
            "Error: invalid literal for int() with base 10: '-1.2345'\nFinished",
            "Negative Float",
        ),
        (
            ["256e-2"],
            "Error: invalid literal for int() with base 10: '256e-2'\nFinished",
            "Scientific",
        ),
        (
            ["-256e-2"],
            "Error: invalid literal for int() with base 10: '-256e-2'\nFinished",
            "Negative Scientific",
        ),
        (
            [""],
            "Error: invalid literal for int() with base 10: ''\nFinished",
            "Empty String",
        ),
        (
            ["Abc"],
            "Error: invalid literal for int() with base 10: 'Abc'\nFinished",
            "String",
        ),
    ]

    def test_problem(self) -> None:
        self._test_problem()
