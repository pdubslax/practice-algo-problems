class Solution(object):
    
    
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(A) > len(B):
            B,A = A,B
        low = 0
        high = len(A) - 1 if len(A) > 0 else 0
        total = (len(A) + len(B) + 1) / 2
        while (True):
            partition = (high + low) / 2
            Alow = A[partition - 1] if partition - 1 >= 0 else float('-inf')
            Ahigh = A[partition] if partition < len(A) else float('inf')
            Blow = B[total - partition - 1] if total - partition - 1 >= 0 else float('-inf')
            Bhigh = B[total - partition] if total - partition < len(B) else float('inf')
            
            if Alow <= Bhigh and Blow <= Ahigh:
                #solution found using these four numbers
                if (len(A) + len(B)) % 2 == 0:
                    # even
                    return (max(Alow,Blow) + min(Ahigh,Bhigh))/2.0
                else: 
                    return max(Alow,Blow)
            elif Alow > Bhigh:
                #slide search toward -inf
                high = partition - 1
                low = high if low > high else low
            else:
                #slide search toward inf
                low = partition + 1
                high = low if high < low else high
            
        