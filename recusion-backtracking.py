

class Recursion:

    def __init__(self):
        pass

    def factorialOf(self, num : int) -> int:
        """
        This function calculates factorial of a number using recursion.
        """
        if num < 0:
            raise ValueError("Only non-negative argument should be passed")
        
        if num == 1:
            return 1
        
        return num * self.factorialOf(num - 1)
    
    def findFibonacci(self, nth_term : int) -> int:
        """
        This function returns the nth term of the fibonacci sequence.
        """
        if nth_term < 0:
            raise ValueError("Only non-negative argument should be passed")
        
        if nth_term == 1:
            return 0
        
        if nth_term == 2:
            return 1
        
        return self.findFibonacci(nth_term - 1) + self.findFibonacci(nth_term - 2)
    
    def sumOf(self, array : list) -> float:
        """
        This function returns the sum of all elements present in the given array.
        """
        if not array:
            return 0
        if len(array) == 1:
            return array[0]

        return self.sumOf(array[0]) + self.sumOf(array[1])
    
if __name__ == "__main__":
    r = Recursion()
    a = [1,2,3,4,5]
    print(r.sumOf(a))
        