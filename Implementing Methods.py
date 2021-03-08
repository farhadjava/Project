
class Teddy:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def change_color(self,color):
        print("This is a method")
        self.color = "Orange"

teddy = Teddy ("Ted","brown")
print(teddy.name)
print(teddy.color)

teddy.change_color("Orange")
print(teddy.name)
print(teddy.color)
