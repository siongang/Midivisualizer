import time

# we dont need this if we use rgbA 
def lighten_colour(colour, increment):
    max_val = max(colour)
    index = colour.index(max_val)


    r = min(int(colour[0] + (255 - colour[0]) * increment), 255)
    g = min(int(colour[1] + (255 - colour[1]) * increment), 255)
    b = min(int(colour[2] + (255 - colour[2]) * increment), 255)

    temp = [r,g,b]
    temp[index] = max_val

    return tuple(temp)

