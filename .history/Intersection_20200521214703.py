 def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = [];
        short = [];
        long = [];
        if len(nums1) > len(nums2):
            long = nums1
            short = nums2
        else:   
            long = nums2
            short = nums1
        for a in long:
            if a in short:
                intersection.append(a)
                short.remove(a)
            
        return intersection 