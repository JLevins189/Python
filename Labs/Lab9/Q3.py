class Rectangle():
    def __init__(self, side1_length, side2_length):
        self.side1length = side1_length
        self.side2length = side2_length
        self.area_rect = side1_length * side2_length
        self.perim_rect = (side2_length * 2) + (side1_length * 2)

    def change_side1(self, side2_length,side1_length):
        self.side1length = side1_length
        self.area_rect = side1_length * side2_length
        self.perim_rect = (side2_length * 2) + (side1_length * 2)

    def change_side2(self, side1_length,side2_length):
        self.side2length = side2_length
        self.area_rect = side1_length * side2_length
        self.perim_rect = (side2_length * 2) + (side1_length * 2)



    def __str__(self):
        return "Side 1 = " + str(self.side1length) + "\n" + "Side 2 = " + str(self.side2length) + "\n" + "Area = " + str(self.area_rect) + "\n" + "Perimeter = " + str(self.perim_rect) + "\n\n"


#main
rectangle1 = Rectangle(1,2)
print(rectangle1)
rectangle1.change_side2(rectangle1.side1length,4)
rectangle1.change_side1(rectangle1.side2length,6)
print(rectangle1)
