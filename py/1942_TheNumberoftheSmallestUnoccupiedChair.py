# 1942. The Number of the Smallest Unoccupied Chair

from utils import chunk
from typing import List
import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        targetArrive, _ = times[targetFriend]
        times.sort()
        # size of depart tells us how many friends are at the party currently
        depart = []
        availableSeats = []

        for arriveTime, departTime in times:
            # clear seats if friend has already departed - arriveTime >= departTime (equal is required)
            while depart and depart[0][0] <= arriveTime:
                _, emptySeat = heapq.heappop(depart)
                # for each friend that leaves, we keep track of this seat to assign the lowest number to the next
                heapq.heappush(availableSeats, emptySeat)

            if arriveTime == targetArrive:
                break

            # we run out of seats if current seating capacity (len(depart)) is equal to number of guests due to depart
            currSeat = len(depart) \
                if len(availableSeats) == 0 \
                else heapq.heappop(availableSeats)

            heapq.heappush(depart, (departTime, currSeat))

        # there are no empty seats, add a seat - zero-indexed
        if len(availableSeats) == 0:
            return len(depart)

        # take the lowest available seat
        return heapq.heappop(availableSeats)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [[1, 4], [2, 3], [4, 6]],
        1,
        [[3, 10], [1, 5], [2, 6]],
        0,
        [[4, 5], [12, 13], [5, 6], [1, 2], [8, 9], [9, 10], [6, 7], [3, 4], [7, 8],
         [13, 14], [15, 16], [14, 15], [10, 11], [11, 12], [2, 3], [16, 17]],
        15
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().smallestChair(*puzzle))
