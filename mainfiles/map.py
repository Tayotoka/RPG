"""
Testing for maps and such. needs a lot of work and planning however
still to do:
Expand map, integrate spawning, move to different maps, and wall collisions
--- this is just for text based, not with a GUI.
"""


class Player(object):

    def __init__(self, name):
        self.name = name

    def movement(self):
        """
        takes players position and returns a new postion
        """
        print(maps.userpos)
        move = input(" [W], [A], [S], [D]: ").lower()  # movement "wasd"
        while True:
            if move == 'w':  # Forward
                x, y = (1, 0)  # x/y = column/row
                break  # applys change
            elif move == 'd':  # right
                x, y = (0, 1)
                break
            elif move == 's':  # backwards
                x, y = (-1, 0)
                break
            elif move == 'a':  # left
                x, y = (0, -1)
                break
            else:
                print("Not a valid direction!")
        a = maps.column + x  # places in tilesmap
        b = maps.row + y     # places in tilesmap
        maps.userpos = tilemap[a][b]
        if maps.userpos == 3:
            print('Loot!')
        return maps.userpos


class World(object):
    """
    defines a world map
    """
    def __init__(self, column, row):
        self.userpos = tilemap[column][row]
        self.column = column
        self.row = row

floor = 0
entry = 1
leave = 2
loot = 3                # tile map w/ variable names
tilemap = [[0, 1, 0],   # [floor, entry, floor]
           [2, 0, 0],   # [loot, floor, floor]
           [0, 3, 0]]   # [floor, exit, floor]

maps = World(0, 0)
hero = Player('Tayotoka')


def main():
    """
    the main game for movement and such
    """
    inp = input('Press any button to continue..: ')
    if inp != '':
        hero.movement()
        print(maps.userpos)

main()
