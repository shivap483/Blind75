


def solution(queries, diff):
    
    numbers = []
    ans = []
    
    def findTriples(nums, diff):
        if len(nums) < 3:
            return 0
        triples = 0
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num, 0)
        nums= sorted(list(set(nums)))
        for i in range(1, len(nums) - 1):
            if nums[i] - nums[i-1] == nums[i+1] - nums[i] == diff:
                triples += map[nums[i-1]] * map [nums[i]] * map[nums[i+1]]
        return triples
        
    
    for query in queries:
        if query[0] == "+":
            numbers.append(int(query[1:]))
        else:
            temp = [x for x in numbers if x != int(query[1:])]
            numbers = temp
        ans.append(findTriples(numbers, diff))
    return ans

a = ["+8", "+10", "+12"]
print(solution(a, 2))