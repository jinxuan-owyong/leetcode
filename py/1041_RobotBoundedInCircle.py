# 1041. Robot Bounded In Circle

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        DIRECTIONS = {
            "N": (-1, 0),
            "S": (1, 0),
            "E": (0, 1),
            "W": (0, -1)
        }
        LEFT = {
            "N": "W",
            "S": "E",
            "E": "N",
            "W": "S"
        }
        RIGHT = {
            "N": "E",
            "S": "W",
            "E": "S",
            "W": "N"
        }

        y, x = 0, 0
        curr = "N"
        for _ in range(4):
            for move in instructions:
                if move == "G":
                    dy, dx = DIRECTIONS[curr]
                    y, x = y + dy, x + dx
                elif move == "L":
                    curr = LEFT[curr]
                else:
                    curr = RIGHT[curr]

        return (y, x) == (0, 0)


if __name__ == "__main__":
    puzzles = [
        "GGLLGG",
        "GG",
        "GL",
        "GLGR",
        "GRGL"
    ]
    for puzzle in puzzles:
        print(Solution().isRobotBounded(puzzle))
