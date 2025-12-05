from typing import List


class Solution:
    def search(self, nums: List[int], target: int, baixo=0, alto=None) -> int:
        if alto == None:
            alto = len(nums)-1

        while baixo < alto:
            meio = int((alto + baixo) / 2)

            if nums[meio] == target:
                return meio
            elif nums[meio] < target:
                baixo = meio + 1
            else:
                alto = meio
        return -1

    def exponential_search(self, arr, target):
        if arr[0] == target:
            return 0
        n = len(arr)
        i = 1

        while i < n and arr[i] < target:
            i *= 2
        if arr[i] == target:
            return i

        return self.search(arr, target, i/2, min(i, n-1))