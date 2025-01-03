import enum


class InvalidCoordinate(Exception):
    pass


class Looping(Exception):
    pass


class Direction(enum.Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


class Result(enum.Enum):
    Init = "Not Ran"
    Left = "Left Map"
    Looping = "Looping"


class Space:
    def __init__(self, walkable):
        self.walkable = walkable


class Free(Space):
    def __init__(self):
        super().__init__(True)

    def __str__(self):
        return "."


class Obstruction(Space):
    def __init__(self):
        super().__init__(False)

    def __str__(self):
        return "#"


class Custom_Obstruction(Obstruction):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "O"


class Vist(Space):
    def __init__(self, direction):
        super().__init__(True)
        self.directions = [direction]

    def __str__(self):
        moved_horiziontally = False
        moved_vertically = False
        if len(set([Direction.LEFT, Direction.RIGHT]) & set(self.directions)) != 0:
            moved_horiziontally = True
        if len(set([Direction.UP, Direction.DOWN]) & set(self.directions)) != 0:
            moved_vertically = True

        if moved_horiziontally and moved_vertically:
            return "+"

        if moved_horiziontally:
            return "-"

        if moved_vertically:
            return "|"

        return "X"

    def add_direction(self, direction):
        if direction in self.directions:
            raise Looping
        else:
            self.directions.append(direction)


class Guard:
    def __init__(self, x, y, direction):
        self.starting_x = x
        self.starting_y = y
        self.starting_direction = Direction(direction)
        self.x = x
        self.y = y
        self.direction = Direction(direction)

    def turn(self):
        match self.direction:
            case Direction.UP:
                self.direction = Direction.RIGHT
            case Direction.DOWN:
                self.direction = Direction.LEFT
            case Direction.LEFT:
                self.direction = Direction.UP
            case Direction.RIGHT:
                self.direction = Direction.DOWN


class Map:
    def __init__(self, lines):
        self.input = lines
        self.starting_map = None
        self.max_y = len(lines) - 1
        self.max_x = len(lines[0]) - 1
        self.spaces = self.parse_input()
        self.result = Result.Init

    def __repr__(self):
        if not self.starting_map:
            self.starting_map = self.parse_input()
        starting_string_map = ""
        finished_string_map = ""
        for y in range(0, self.max_y + 1):
            for x in range(0, self.max_x + 1):
                if y == self.guard.starting_y and x == self.guard.starting_x:
                    starting_string_map += self.guard.starting_direction.value
                    finished_string_map += str(self.spaces[y][x])
                elif y == self.guard.y and x == self.guard.x:
                    finished_string_map += self.guard.direction.value
                    starting_string_map += str(self.starting_map[y][x])
                else:
                    starting_string_map += str(self.starting_map[y][x])
                    finished_string_map += str(self.spaces[y][x])
            starting_string_map += "\n"
            finished_string_map += "\n"

        message = [
            "Starting Map:",
            starting_string_map,
            "" "Finished Map:",
            finished_string_map,
            f"Result: {self.result.value}",
        ]
        return "\n".join(message)

    def parse_input(self):
        output = []
        for line in self.input:
            output.append(list(line))
        for y in range(0, self.max_y + 1):
            for x in range(0, self.max_x + 1):
                value = output[y][x]
                if value in Direction:
                    self.guard = Guard(x, y, value)
                    output[y][x] = Vist(value)
                else:
                    match value:
                        case ".":
                            output[y][x] = Free()
                        case "#":
                            output[y][x] = Obstruction()
                        case "O":
                            output[y][x] = Custom_Obstruction()
        return output

    def get_value(self, x, y):
        if x > self.max_x:
            raise InvalidCoordinate
        if x < 0:
            raise InvalidCoordinate
        if y > self.max_y:
            raise InvalidCoordinate
        if y < 0:
            raise InvalidCoordinate

        return self.spaces[y][x]

    def mark_as_visited(self, x, y, direction):
        if isinstance(self.spaces[y][x], Vist):
            self.spaces[y][x].add_direction(direction)
        else:
            self.spaces[y][x] = Vist(direction)

    def add_custom_obstruction(self, x, y):
        self.spaces[y][x] = Custom_Obstruction()

    def count_visited(self):
        total = 0
        for y in range(0, self.max_y + 1):
            for x in range(0, self.max_x + 1):
                if isinstance(self.get_value(x, y), Vist):
                    total += 1
        return total

    def get_all_visited_locations(self):
        locations = []
        for y in range(0, self.max_y + 1):
            for x in range(0, self.max_x + 1):
                if x == self.guard.starting_x and y == self.guard.starting_y:
                    continue
                elif isinstance(self.get_value(x, y), Vist):
                    locations.append((x, y))
        return locations

    def move_guard(self):
        start_x, start_y = self.guard.x, self.guard.y
        match self.guard.direction:
            case Direction.UP:
                next_x, next_y = start_x, start_y - 1
            case Direction.DOWN:
                next_x, next_y = start_x, start_y + 1
            case Direction.LEFT:
                next_x, next_y = start_x - 1, start_y
            case Direction.RIGHT:
                next_x, next_y = start_x + 1, start_y
        next_space = self.get_value(next_x, next_y)
        if next_space.walkable:
            self.mark_as_visited(next_x, next_y, self.guard.direction)
            self.guard.x, self.guard.y = next_x, next_y
            return True
        return False

    def turn_guard(self):
        self.guard.turn()
        self.mark_as_visited(self.guard.x, self.guard.y, self.guard.direction)

    def run(self):
        for _ in range(0, 10000):
            try:
                if not self.move_guard():
                    self.turn_guard()
            except InvalidCoordinate:
                self.result = Result.Left
                break
            except Looping:
                self.result = Result.Looping
                break


def parse_file(filename: str):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        return lines
