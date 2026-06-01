class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        nums3 = []
        while(i < m and j < n):
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i = i + 1
            else:
                nums3.append(nums2[j])
                j = j + 1
        nums3.extend(nums2[j:n])
        nums3.extend(nums1[i:m])

        for i in range(m+n):
            nums1[i] = nums3[i]

                

        