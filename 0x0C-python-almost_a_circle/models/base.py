#!/usr/bin/python3
'''Base class.'''

class Base:
 '''A base of object oriented programming'''

   __nb_objects = 0

   def __init__(self, id=None):
      '''Constructor.'''
   if id is not None:
      self.id = id
   else:
      Base.__nb_objects +=1
      self.id = Base.__nb_objects
