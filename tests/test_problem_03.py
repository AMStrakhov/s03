from typing import Callable, List, Tuple

from problem_03 import count_ones
from .base_test_problem import BaseTestProblem


class TestProblem03(BaseTestProblem):
    _problem_func: Callable = count_ones
    cases: List[Tuple[List, str, str]] = [
        ([0], 0, "0"),
        ([1], 1, "1"),
        ([50], 3, "50"),
        ([50], 3, "50"),
    ]
    modules_to_patch: List[str] = ["builtins.bin"]

    def test_function(self) -> None:
        self._test_function()

    def test_exception(self) -> None:
        cases = [-1, -1.5, "abc", [1, 2, 3], {"a": "b"}]
        for case in cases:
            with self.subTest(case):
                with self.assertRaises(Exception):
                    self.problem_func(case)
