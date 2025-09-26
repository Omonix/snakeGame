from maillon import Maillon

class Snake():
    def __init__(self):
        self.__pos = Maillon((30, 0), None)
        self.__to = "bottom"
    def handle_to(self, to):
        self.__to = to
    def read_to(self):
        return self.__to
    def read_pos(self):
        return self.__pos
    def read_head(self):
        return self.__pos.pos
    def add_head(self):
        direction = {"top": (0, -10), "bottom": (0, 10), "left": (-10, 0), "right": (10, 0)}
        new_x, new_y = self.__pos.pos[0] + direction[self.__to][0], self.__pos.pos[1] + direction[self.__to][1]
        self.__pos = Maillon((new_x, new_y), self.__pos)
    def __remove_last(self, m):
        if m.point.point == None:
            m.point = None
        else:
            self.__remove_last(m.point)
    def cut_tail(self):
        self.__remove_last(self.__pos)
    def __length(self, m):
        if m.point == None:
            return 1
        else:
            return 1 + self.__length(m.point)
    def get_length(self):
        return self.__length(self.__pos)
    def is_in_snake(self, v, m):
        if m.point == None:
            return False
        else:
            if m.pos == v:
                return True
            else:
                return self.is_in_snake(v, m.point)
    def is_dead(self):
        head = self.read_head()
        return self.is_in_snake(head, self.__pos.point)
