import ctypes


class ArrayClass():

    arr_list = []

    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1   # Default Capacity
        self.A = self.make_array(self.capacity)
        self.__class__.arr_list.append(self)

    # def add(self, val):
    #         """
    #         Add element to end of the array
    #         """
    #         if self.n == self.capacity:
    #             # Double capacity if not enough room
    #             self._resize(2 * self.capacity)
        
    #         self.A[self.n] = val  # Set self.n index to element
    #         self.n += 1

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n

    def __get__(self, i):
        """
        Return element at index i
        """
        if not 0 <= i < self.n:
            # Check it i index is in bounds of array
            return IndexError('i is out of bounds !')

        return self.A[i]   # Retrieve from the array at index i

    def __set__(self, val, i):
        """
         This function inserts the item at any specified index
        """
        if i < 0 or i > self.n:
            print("please enter appropriate index..")
            return

        if self.n == self.capacity:
            self._resize(2*self.capacity)
  
        for j in range(self.n - 1, i - 1, - 1):
            self.A[j+1] = self.A[j]

        self.A[i] = val
        self.n += 1
    
    def _resize(self, nw_cap): 
        """ 
        Resize internal array to capacity new_cap
        """
        
        B = self.make_array(nw_cap) # New bigger array

        for k in range(self.n): # Reference all existing values
            B[k] = self.A[k]
              
        self.A = B # Call A the new bigger array
        self.capacity = nw_cap # Reset the capacity
          
    def make_array(self, nw_cap): 
        """ 
        Returns a new array with new_cap capacity
        """
        return (nw_cap * ctypes.py_object)()

array1 = ArrayClass()
