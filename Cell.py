import random

nucleotides = ['a', 't', 'g', 'c']

# main class for a cell
class Cell():

    # basics of the cell
    def __init__(self, world_x:int, world_y:int):
        self.x_pos = random.randint(10, world_x-10)
        self.y_pos = random.randint(10, world_y-10)
        self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        self.speed = round(random.uniform(0, 1), 2)
        self.size = random.randint(5, 10)

        self.genome = Genome().gen_str

    # movement of cell
    def move(self):
        self.x_pos += random.randint(-10, 10) * self.speed
        self.y_pos += random.randint(-10, 10) * self.speed


class Genome:
    # basics of genome
    def __init__(self):
        self.gen_str = ''.join(random.choices(nucleotides, k=12))


class Gen:
    pass





