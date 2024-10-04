# 2491. Divide Players Into Teams of Equal Skill

from utils import chunk
from typing import List
from collections import Counter


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chemistry = sum(skill)
        n = len(skill) // 2  # length is even

        # not possible to divide chemistry each team equally
        if chemistry % n > 0:
            return -1

        teamSkill = chemistry // n
        count = Counter(skill)
        result = 0
        seen = set()
        for player in count:
            if player in seen:
                continue

            required = teamSkill - player
            # skill of both players must add up to the team skill
            if required not in count or count[player] != count[required]:
                return -1

            seen.update([player, required])
            # avoid double counting if both players have the same level
            if player == required:
                result += count[player] // 2 * player * required
            else:
                result += count[player] * player * required

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [3, 2, 5, 1, 3, 4],
        [3, 4],
        [1, 1, 2, 3],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().dividePlayers(*puzzle))
