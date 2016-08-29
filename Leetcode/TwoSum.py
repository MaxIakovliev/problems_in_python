class TwoSum:
    def solution1(self, nums, target):
        result = [-1, -1]
        storage = {}
        for i, val in enumerate(nums):
            if nums[i] in storage:
                result[0] = storage[nums[i]]
                result[1] = i
                return result
            else:
                tmp = target - nums[i]
                if tmp not in storage:
                    storage[tmp] = i

        return result


p = TwoSum()
result = p.solution1([1, 2, 3, 5], 4)
print(result)
