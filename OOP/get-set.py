#capsule =set/get
#content 0.......100


class Box:
        def __getattr__(self, name):
                  if name == "content":
                     return   self.__dict__[name]
        def __setattr__(self,name , value):
                
                if name == "content" and value >=0 and value <=100:
                        self.__dict__[name] = value
                else:
                       print("Wrong attribute or value")

                       




# ------------------------
#|                       |
#|                       <----------setter
#|        value          |
#|                       |
#|                       ----------->getter
#|                       |
#-------------------------

b1= Box()
# b2= Box()

b1.content = 1
# b2.content = 100

print(b1.content)
#print(b2.jhigyfui)