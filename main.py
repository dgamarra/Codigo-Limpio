"""Calcula el area de un rectángulo o un cuadrado"""
def calculate_area(length, width=None):
    """ Calculo del area"""
    if width is None:
        width = length
    return length * width

if __name__=="__main__":
    length_rectangle = 5
    width_rectangle = 3
    side_square = 4

    print(f"Rectangle area: {calculate_area(length_rectangle, width_rectangle)}")
    print(f"Square area: {calculate_area(side_square)}")
