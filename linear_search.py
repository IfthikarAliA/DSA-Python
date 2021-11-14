
def search(nums, target):
    for i in range(len(nums)):
        if(nums[i]==target):
            return i
    return -1

nums = [1,2,3,4,5]
target=int(input())
result = search(nums,target)
print(f"The target is found at {result} Index")