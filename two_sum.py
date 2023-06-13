import asyncio


class Solution:
    @staticmethod
    async def find_indices(nums, target):
        adds = {}
        for i, num in enumerate(nums):
            add = target - num
            if add in adds:
                return [adds[add], i]
            adds[num] = i
            await asyncio.sleep(0)
        return []

    @staticmethod
    async def two_sum(nums, target):
        return await Solution.find_indices(nums, target)


# Test the solution
nums = [2, 7, 11, 15]
target = 9

async def main():
    result = await Solution.two_sum(nums, target)
    print(result)

asyncio.get_event_loop().run_until_complete(main())
