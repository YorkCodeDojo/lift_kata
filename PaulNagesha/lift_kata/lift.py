from enum import Enum


class Direction(Enum):
    STOP = 0
    UP = 1
    DOWN = 2


class Shard:
    height = 309.6
    num_floors = 95
    num_lifts = 36
    speed_m_per_s = 6


class Lift:
    current_floor: int
    direction: Direction
    target_floor_up: set[int]
    target_floor_down: set[int]

    @property
    def target_floor(self):
        sorted_up = list(self.target_floor_up)
        sorted_up.sort()
        sorted_down = list(self.target_floor_down)
        sorted_down.sort(reverse=True)
        return sorted_up + sorted_down \
            if self.direction == Direction.UP \
            else sorted_down + sorted_up

    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        self.target_floor_up = set()
        self.target_floor_down = set()
        self.direction = Direction.STOP

    def push_floor_button(self, floor: int):
        if len(self.target_floor) == 0:
            if floor < self.current_floor:
                self.direction = Direction.DOWN
            elif floor > self.current_floor:
                self.direction = Direction.UP
            else:
                self.direction = Direction.STOP

        if self.current_floor < floor:
            self.target_floor_up = {*self.target_floor_up, floor}
        elif floor < self.current_floor:
            self.target_floor_down = {*self.target_floor_down, floor}

    def move(self):
        self.current_floor += (1 if self.direction == Direction.UP else -1 if self.direction == Direction.DOWN else 0)

        if self.current_floor in self.target_floor_up:
            self.target_floor_up.remove(self.current_floor)
        elif self.current_floor in self.target_floor_down:
            self.target_floor_down.remove(self.current_floor)

        if self.direction == Direction.UP and len(self.target_floor_up) == 0:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN and len(self.target_floor_down) == 0:
            self.direction = Direction.UP
