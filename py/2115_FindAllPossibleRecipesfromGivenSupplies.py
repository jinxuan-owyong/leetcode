# 2115. Find All Possible Recipes from Given Supplies

from utils import chunk
from typing import List
from collections import deque
from collections import defaultdict


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        since the recipes can also be used as ingredients for other recipes, 
        we need to find the topological ordering of recipes first
        recipes and ingredients are nodes, and edges are ingredients[i][j] -> recipes[i]
        """
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        for i, items in enumerate(ingredients):
            for ing in items:
                adjList[ing].append(recipes[i])
                indegree[recipes[i]] += 1

        # with the prerequisite graph, we can find the topological ordering with kahn's algorithm
        # use each supply as a starting node. if it is not present, then indegree is not decremented
        order = []
        queue = deque(supplies)
        recipes = set(recipes)
        while queue:
            curr = queue.popleft()
            if curr in recipes:
                order.append(curr)
            for nei in adjList[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return order


if __name__ == "__main__":
    testSize = 3
    puzzles = [
        ["bread"],
        [["yeast", "flour"]],
        ["yeast", "flour", "corn"],
        ["bread", "sandwich"],
        [["yeast", "flour"], ["bread", "meat"]],
        ["yeast", "flour", "meat"],
        ["bread", "sandwich", "burger"],
        [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
        ["yeast", "flour", "meat"],
        ["bread"],
        [["yeast", "flour"]],
        ["yeast"],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findAllRecipes(*puzzle))
