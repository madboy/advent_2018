from collections import defaultdict
from dataclasses import dataclass
from src.tools import left_pad_process


@dataclass(eq=True, frozen=True)
class Pos:
    x: int
    y: int


directions = {"<": 0, "^": 1, ">": 2, "v": 3}
turns = [-1, 0, 1]  # left, straight, right


@dataclass
class Cart:
    p: Pos
    direction: int
    turn: int  # which way I should turn, starting value should be 0
    # turn should be index into turns -1, 0, 1, and we incr index % 3
    # this then resolves into which direction we move


@dataclass
class Section:
    rail: str
    p: Pos


def run(input_file):
    # --------------------------- Setup initial state ---------------------------
    y = 0
    sections = {}
    carts = []
    for line in left_pad_process(input_file):
        x = 0
        for c in line:
            if c == " ":  # we don't need to save spaces
                pass
            elif c in [">", "<"]:
                sections[Pos(x, y)] = "-"
                carts.append(Cart(Pos(x, y), directions[c], 0))
            elif c in ["^", "v"]:
                sections[Pos(x, y)] = "|"
                carts.append(Cart(Pos(x, y), directions[c], 0))
            else:
                sections[Pos(x, y)] = c
            x += 1
        y += 1

    print(carts)

    # --------------------------- Ticks until first crash ---------------------------
    collision = False
    while not collision:
        positions = defaultdict(int)
        for cart in carts:
            if cart.direction == 0:
                new_pos = Pos(cart.p.x - 1, cart.p.y)
                next_section = sections[new_pos]
            elif cart.direction == 1:
                new_pos = Pos(cart.p.x, cart.p.y - 1)
                next_section = sections[new_pos]
            elif cart.direction == 2:
                new_pos = Pos(cart.p.x + 1, cart.p.y)
                next_section = sections[new_pos]
            elif cart.direction == 3:
                new_pos = Pos(cart.p.x, cart.p.y + 1)
                next_section = sections[new_pos]

            cart.p = new_pos
            if next_section in ["-", "|"]:
                pass
            elif next_section == "+":
                cart.direction = (cart.direction + turns[cart.turn]) % 4
                cart.turn = (cart.turn + 1) % 3
            elif next_section == "\\" and cart.direction in [1, 3]:
                cart.direction = (cart.direction - 1) % 4
            elif next_section == "\\" and cart.direction in [0, 2]:
                cart.direction = (cart.direction + 1) % 4
            elif next_section == "/" and cart.direction in [1, 3]:
                cart.direction = (cart.direction + 1) % 4
            elif next_section == "/" and cart.direction in [0, 2]:
                cart.direction = (cart.direction - 1) % 4

            positions[cart.p] += 1

        for k, v in positions.items():
            if v > 1:
                print(k)
                collision = True
