import textwrap
import unittest

import icontract_hypothesis

from correct_programs.aoc2020 import day_22_crab_combat


class TestWithIcontractHypothesis(unittest.TestCase):
    def test_compute_score(self) -> None:
        icontract_hypothesis.test_with_inferred_strategy(
            day_22_crab_combat.compute_score
        )


class TestManually(unittest.TestCase):
    def test_case(self) -> None:
        lines = textwrap.dedent(
            """\
            Player 1:
            9
            2
            6
            3
            1
            
            Player 2:
            5
            8
            4
            7
            10"""
        ).splitlines()

        cards1, cards2 = day_22_crab_combat.parse_lines(lines=lines)

        deck1 = day_22_crab_combat.Deck(cards=cards1)
        deck2 = day_22_crab_combat.Deck(cards=cards2)

        split = day_22_crab_combat.Split(deck1=deck1, deck2=deck2)

        final_split = day_22_crab_combat.play(split=split)

        score1 = day_22_crab_combat.compute_score(final_split.deck1)
        score2 = day_22_crab_combat.compute_score(final_split.deck2)

        self.assertEqual(306, max(score1, score2))


if __name__ == "__main__":
    unittest.main()