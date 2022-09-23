from typing import Callable, List, Tuple

from problem_08 import sum_of_digits
from .base_test_problem import BaseTestProblem


class TestProblem08(BaseTestProblem):
    _problem_func: Callable = sum_of_digits
    cases: List[Tuple[List, str, str]] = [
        ([0], 0, "0"),
        ([1], 1, "1"),
        ([50], 5, "50"),
        ([256], 13, "256"),
        ([-256], 13, "-256"),
        ([1111000011110000], 8, "1111000011110000"),

    ]
    modules_to_patch: List[str] = ["builtins.sum"]

    def test_function(self) -> None:
        self._test_function()
