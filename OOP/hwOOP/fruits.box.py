class FruitBox:
  def __init__(self,apples,oranges):
    if (apples+oranges)>50 :
      print("Warning value too high")
    elif  not isinstance(apples, int) or not isinstance(oranges, int):
        print("Numbers are not integers")
    else:
        self.apples = apples
        self.oranges = oranges
  def __add__(self, box2):
        total_apples = self.apples + box2.apples
        total_oranges = self.oranges + box2.oranges
        return FruitBox(total_apples, total_oranges)
         
  def __str__(self):
     return f"Fruit box contains{self.apples} apples and {self.oranges} oranges"
#def add(self, other_box):
       

a_box = FruitBox(5,20)
b_box = FruitBox(2,8)
c_box= a_box + b_box

print(c_box)