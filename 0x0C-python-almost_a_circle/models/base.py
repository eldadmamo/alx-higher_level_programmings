#!/usr/bin/python3
'''
Base class.
'''

class Base:
 '''
A base of object oriented programming
'''

   __nb_objects = 0

   def __init__(self, id=None):
      '''Constructor.'''
   if id is not None:
      self.id = id
   else:
      Base.__nb_objects += 1
      self.id = Base.__nb_objects


if __name__ = "__main__";

     b1 = Base()
     print(b1.id)

     b2 = Base()
     print(b2.id)

     b3 = Base()
     print(b3.id)
 
     b4 = Base()
     print(b4.id)

     b5 = Base()
     print(b5.id)
