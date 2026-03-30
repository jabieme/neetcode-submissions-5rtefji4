class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(m, m+n):
            nums1[i] = nums2[j]
            j+=1

        def mergeSort(arr, s, e):
            if e - s + 1 <= 1:
                return arr
            
            mid = (s+e) // 2
            mergeSort(arr, s, mid)
            mergeSort(arr, mid+1, e)

            self.bigMerge(arr, s, mid, e)

            return arr

        return mergeSort(nums1, 0, m+n-1)
        
    def bigMerge(self, arr, s, m, e):
        L = arr[s:m+1]
        R = arr[m+1:e+1]

        i = 0
        j = 0
        k = s

        while len(L) > i and len(R) > j:
            if L[i] >= R[j]:
                arr[k] = R[j]
                j+=1
                k+=1
            else:
                arr[k] = L[i]
                i+=1
                k+=1
        while len(L) > i:
            arr[k] = L[i]
            i+=1
            k+=1
        while len(R) > j:
            arr[k] = R[j]
            j+=1
            k+=1  
        

        