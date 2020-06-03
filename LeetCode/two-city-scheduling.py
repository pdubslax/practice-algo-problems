class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key = lambda x : x[0] - x[1])
        return sum([i[0] for i in costs[:len(costs)/2]]) + sum([i[1] for i in costs[len(costs)/2:]])
        