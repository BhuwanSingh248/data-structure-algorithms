class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort()
        [queue.append(i) for i in range(len(deck))]
        op = [None] * len(deck)
        count = 0

        for i in range(len(deck)):
            op[queue.popleft()] =  deck[i]
            if(queue):
                queue.append(queue.popleft())
        return op