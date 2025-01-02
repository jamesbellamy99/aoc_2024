import enum


class Direction(enum.Enum):
    UP = enum.auto()
    DOWN = enum.auto()
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP_LEFT = enum.auto()
    UP_RIGHT = enum.auto()
    DOWN_LEFT = enum.auto()
    DOWN_RIGHT = enum.auto()


class InvalidCoordinate(Exception):
    pass


class Grid:
    def __init__(self, lines):
        self.max_y = len(lines) - 1
        self.max_x = len(lines[0]) - 1
        self.letters = lines

    def __repr__(self):
        return f"Max Y:{self.max_y}\nMax X:{self.max_x}\nLetters:\n{"\n".join(self.letters)}"

    def get_letter(self, x, y):
        if x > self.max_x:
            raise InvalidCoordinate
        if x < 0:
            raise InvalidCoordinate
        if y > self.max_y:
            raise InvalidCoordinate
        if y < 0:
            raise InvalidCoordinate

        return self.letters[y][x]

    def get_letters_in_direction(
        self, starting_x: int, starting_y: int, direction: Direction, length: int = 3
    ):
        coordinates = []
        for i in range(1, length + 1):
            match (direction):
                case Direction.UP:
                    coordinates.append((starting_x, starting_y - i))
                case Direction.DOWN:
                    coordinates.append((starting_x, starting_y + i))
                case Direction.RIGHT:
                    coordinates.append((starting_x + i, starting_y))
                case Direction.LEFT:
                    coordinates.append((starting_x - i, starting_y))
                case Direction.DOWN_RIGHT:
                    coordinates.append((starting_x + i, starting_y + i))
                case Direction.DOWN_LEFT:
                    coordinates.append((starting_x - i, starting_y + i))
                case Direction.UP_RIGHT:
                    coordinates.append((starting_x + i, starting_y - i))
                case Direction.UP_LEFT:
                    coordinates.append((starting_x - i, starting_y - i))
        result = ""
        for x, y in coordinates:
            result += self.get_letter(x, y)
        return result


def parse_file(filename: str):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        return Grid(lines)
