import ctypes #For using the data types of C

class MeraList:

  def __init__(self):
    self.size = 1 #represents the size of array
    self.n = 0 #represents the no. of elements present in array
    self.Array =  self.__create_array(self.size);

  def __len__(self):
    return self.n

  def __create_array(self, capacity):
    #Creates a c type array (static & referential) with size as capacity
    return (capacity * ctypes.py_object)()

  def __resize(self, new_capacity):
    return (new_capacity * ctypes.py)
  
  def append(self, element):
    if (self.size > self.n):
      self.Array[self.n] = element
      self.n += 1
    else:
      temp = self.__create_array(2 * self.n)
      for i in range(self.n):
        temp[i] = self.Array[i]
      temp[self.n] = element
      self.Array = temp
      self.n += 1
