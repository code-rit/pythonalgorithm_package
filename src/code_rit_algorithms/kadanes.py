
class Kadanes:
    '''
    This function excepts a array of integers to find maximum subarray sum
    '''

    def __init__(self,arr):
        self.arr=arr
        

    def solve(self):
        nums=self.arr
        maxi_so_far=-1000000
        maxi_end_here=0
        for i in nums:
            maxi_end_here=maxi_end_here+i
            maxi_so_far=max(maxi_so_far,maxi_end_here)
            if(maxi_end_here<0):
                maxi_end_here=0
        return maxi_so_far

