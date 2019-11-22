from dataclasses import dataclass
from src.tools import left_pad_process


@dataclass(eq=True)
class Pos:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self


directions = {"<": 0, "^": 1, ">": 2, "v": 3}
turns = [-1, 0, 1]  # left, straight, right


@dataclass
class Cart:
    p: Pos
    direction: int
    turn: int  # which way I should turn, starting value should be 0
    # turn should be index into turns -1, 0, 1, and we incr index % 3
    # this then resolves into which direction we move
    dead: bool

    def __le__(self, other):
        return (self.p.y, self.p.x) <= (other.p.y, other.p.x)

    def __lt__(self, other):
        return (self.p.y, self.p.x) < (other.p.y, other.p.x)


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
            if c == " ":  # we don't need to save spaces or - |
                pass
            elif c in [">", "<"]:
                carts.append(Cart(Pos(x, y), directions[c], 0, False))
            elif c in ["^", "v"]:
                carts.append(Cart(Pos(x, y), directions[c], 0, False))
            else:
                sections[Pos(x, y)] = c
            x += 1
        y += 1

    print(carts)
    # --------------------------- Ticks until first crash ---------------------------
    # directions = {"<": 0, "^": 1, ">": 2, "v": 3}
    movement = [Pos(-1, 0), Pos(0, -1), Pos(1, 0), Pos(0, 1)]
    while len(carts) > 1:
        carts.sort()
        for cart in carts:
            if cart.dead:
                continue
            new_pos = cart.p + movement[cart.direction]

            cart.p = new_pos
            for other_cart in carts:
                if (
                    other_cart != cart
                    and other_cart.p == cart.p
                    and not other_cart.dead
                ):
                    other_cart.dead = True
                    cart.dead = True
                    break
            if cart.dead:
                continue

            next_section = sections.get(cart.p)

            if next_section == "+":
                cart.direction = (cart.direction + turns[cart.turn]) % 4
                cart.turn = (cart.turn + 1) % 3
            elif next_section == "\\":
                if cart.direction in [1, 3]:
                    cart.direction = (cart.direction - 1) % 4
                else:
                    cart.direction = (cart.direction + 1) % 4
            elif next_section == "/":
                if cart.direction in [1, 3]:
                    cart.direction = (cart.direction + 1) % 4
                else:
                    cart.direction = (cart.direction - 1) % 4

        carts = [cart for cart in carts if not cart.dead]
    print(carts)
