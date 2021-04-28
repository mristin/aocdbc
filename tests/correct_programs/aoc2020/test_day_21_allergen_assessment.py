import textwrap
import unittest

import icontract_hypothesis

from correct_programs.aoc2020.day_21_allergen_assessment import (
    parse_list_of_foods,
    solve,
    is_equal_ingredient_list,
)


class TestWithIcontractHypothesis(unittest.TestCase):
    def test_parse_list_of_foods(self) -> None:
        icontract_hypothesis.test_with_inferred_strategy(parse_list_of_foods)

    def test_is_equal_ingredient_list(self) -> None:
        icontract_hypothesis.test_with_inferred_strategy(is_equal_ingredient_list)


class ManualTests(unittest.TestCase):
    def test_solve(self) -> None:
        puzzle_input = textwrap.dedent(
            """\
            mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
            trh fvjkl sbzzf mxmxvkd (contains dairy)
            sqjhc fvjkl (contains soy)
            sqjhc mxmxvkd sbzzf (contains fish)"""
        )

        expected_output = {"kfcds", "nhms", "sbzzf", "trh"}

        self.assertEqual(expected_output, solve(puzzle_input))


if __name__ == "__main__":
    unittest.main()
