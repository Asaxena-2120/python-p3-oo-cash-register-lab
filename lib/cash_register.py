#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self,discount=0):
    self.discount = discount
    self.total=0
    self.items=[]

  def add_item(self,title="eggs",price=0,quantity=1):
    self.last_transaction = price * quantity
    self.total += self.last_transaction
    for _ in range(quantity):
      self.items.append(title)
  def apply_discount(self):
    if (self.discount==0):
      print("There is no discount to apply.")
    else:
      self.total-=self.discount*10
      print(f"After the discount, the total comes to ${self.total}.")
  
  def void_last_transaction(self):
    self.total -= self.last_transaction
