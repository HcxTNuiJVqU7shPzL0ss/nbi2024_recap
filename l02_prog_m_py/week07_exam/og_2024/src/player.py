# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund
#
# Exam
#
#####################################################################


class Player:
    # noqa
    marker = "@"

    def __init__(self, x, y):
        # noqa
        self.pos_x = x
        self.pos_y = y

    # Move the player, "dx" and "dy" is the difference
    def move(self, dx, dy):
        # noqa
        """Moves the player.\n
        dx = horizontal movement, from left to right\n
        dy = vertical movement, from up to down"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        # noqa
        check_x = self.pos_x + x
        check_y = self.pos_y + y
        check_wall = grid.get(check_x , check_y)

        if check_wall == grid.wall: # "■":
            print("Not allowed to walk through walls!")
            input("Press Enter to continue!")
            return False
        else:
            return True

