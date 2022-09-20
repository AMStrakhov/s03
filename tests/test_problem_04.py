from typing import Callable, List, Tuple

from problem_04 import main
from .base_test_problem import BaseTestProblem


class TestProblem04(BaseTestProblem):
    _problem_func: Callable = main
    cases: List[Tuple[List, str, str]] = [
        (["0"], "True", "Zero"),
        (["1"], "True", "Integer"),
        (["-1"], "True", "Negative Integer"),
        (["1.2345"], "True", "Float"),
        (["-1.2345"], "True", "Negative Float"),
        (["256e-2"], "True", "Scientific"),
        (["-256e-2"], "True", "Negative Scientific"),
        ([""], "False", "Empty String"),
        (["Abc"], "False", "String"),
    ]

    def test_problem(self) -> None:
        self._test_problem()
