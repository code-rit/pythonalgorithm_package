class Countsort:
    '''Changes a given array to sorted form in O(n) time O(max) space complexity'''
    def __init__(self,array) -> None:
        self.array=array
        
    def solve(self):
        size = len(self.array)
        output = []
        count = [0] * (max(self.array)+1)
        for i in range(0, size):
            count[self.array[i]] += 1
        for i in range(0, len(count)):
            while(count[i]!=0):
                count[i]=count[i]-1
                output.append(i)
        for i in range(0, size):
            self.array[i] = output[i]

class BubbleSort:
    '''Returns sorted array with time complexity of O(n^2) and space complexity O(1)'''
    def __init__(self,array) -> None:
        self.array=array

    def solve(self):
        for i in range(len(self.array)):
            for j in range(0, len(self.array) - i - 1):
                if self.array[j] >self. array[j + 1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = temp


class SelectionSort:
    '''It  sorts an array with O(N^2) time and O(1) space complexity with reduced number of swaps'''
    def __init__(self,array) -> None:
        self.array=array

    def solve(self):
        size=len(self.array)
        for step in range(size):
            min_idx = step

            for i in range(step + 1, size):
                if self.array[i] < self.array[min_idx]:
                    min_idx = i
            (self.array[step], self.array[min_idx]) = (self.array[min_idx], self.array[step])

