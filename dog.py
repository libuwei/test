class Dog(object):
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def eat(self,food):
    print('%s is eating %s'%(self.name,food))
