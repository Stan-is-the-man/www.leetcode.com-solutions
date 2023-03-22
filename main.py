def removeElement(nums: list[int], val: int):
    while val in nums:
        nums.remove(val)
    return len(nums)

z = [3,2,2,3]
a = removeElement(z, 3)
print(a)

