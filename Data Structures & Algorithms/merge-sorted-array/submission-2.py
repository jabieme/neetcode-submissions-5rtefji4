class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(m, m+n):
            nums1[i] = nums2[j]
            j+=1
        return self.quickSort(nums1, 0, len(nums1)-1)

    def quickSort(self, arr, s, e):
        if e-s+1 <= 1:
            return arr

        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i] < pivot:
                arr[i], arr[left] = arr[left], arr[i]
                left +=1
        
        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSort(arr, s, left-1)
        self.quickSort(arr, left+1, e)

        return arr