class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for i in range(0,len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else :
                odd.append(A[i])
        A = []
        for i in range(0,len(even)):
            A.append(even[i])
            A.append(odd[i])
        return (A)
