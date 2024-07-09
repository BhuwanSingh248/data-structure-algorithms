class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time = customers[0][1]
        current_time = customers[0][0] + customers[0][1]


        for i, j in customers[1:]:
            if i > current_time:
                waiting_time += j
                current_time += i - current_time + j
            else:
                current_time += j
                waiting_time += current_time - i
        print(waiting_time)
        return waiting_time / len(customers)


# [[5,2],[5,4],[10,3],[20,1]]