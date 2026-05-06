class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1) + len(nums2)) // 2

        if len(nums1) < len(nums2):
            smaller = nums1
            larger = nums2
        else:            
            smaller = nums2
            larger = nums1
        
        left = 0
        right = len(smaller) - 1
        while True:
                smaller_mid = (left + right) // 2
                larger_mid = half - smaller_mid - 2

                smaller_left = smaller[smaller_mid] if smaller_mid >= 0 else float("-infinity")
                smaller_right = smaller[smaller_mid + 1] if (smaller_mid + 1) < len(smaller) else float("infinity")

                larger_left = larger[larger_mid] if larger_mid >= 0 else float("-infinity")
                larger_right = larger[larger_mid + 1] if (larger_mid + 1) < len(larger) else float("infinity")

                if smaller_left <= larger_right and larger_left <= smaller_right:
                    if (len(smaller) + len(larger)) % 2:
                        return min(smaller_right, larger_right)
                    return (max(smaller_left, larger_left) + min(smaller_right, larger_right)) / 2
                elif smaller_left > larger_right:
                    right = smaller_mid - 1
                else:
                    left = smaller_mid + 1