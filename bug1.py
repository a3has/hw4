class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def shape(self):
        return "This is a base shape"

    def draw(self):
        return "draw base shape from base class"


class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def shape(self):
        return "This is a circle"

    def draw(self):
        return f"""
({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """


def main():
    c = Circle(1, 2, 3)
    print(c.shape())
    print(c.draw())


main()
