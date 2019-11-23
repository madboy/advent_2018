from dataclasses import dataclass
from src.tools import left_pad_process, turn


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


directions = {"<": "left", "^": "up", ">": "right", "v": "down"}
dturns = {0: "left", 1: "straight", 2: "right"}


@dataclass
class Cart:
    p: Pos
    d: str
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
            elif c in ["<", "^", ">", "v"]:
                carts.append(Cart(p=Pos(x, y), turn=0, dead=False, d=directions[c],))
            else:
                sections[Pos(x, y)] = c
            x += 1
        y += 1

    print(carts)
    # --------------------------- Ticks until first crash ---------------------------
    dmovement = {
        "left": Pos(-1, 0),
        "up": Pos(0, -1),
        "right": Pos(1, 0),
        "down": Pos(0, 1),
    }
    while len(carts) > 1:
        carts.sort()
        for cart in carts:
            if cart.dead:
                continue
            new_pos = cart.p + dmovement[cart.d]

            cart.p = new_pos
            for other_cart in carts:
                if (
                    other_cart != cart
                    and other_cart.p == cart.p
                    and not other_cart.dead
                ):
                    print(cart.p)
                    other_cart.dead = True
                    cart.dead = True
                    break
            if cart.dead:
                continue

            next_section = sections.get(cart.p)

            if next_section == "+":
                cart.d = turn(cart.d, dturns[cart.turn])
                cart.turn = (cart.turn + 1) % 3
            elif next_section == "\\":
                if cart.d in ["up", "down"]:
                    cart.d = turn(cart.d, "left")
                else:
                    cart.d = turn(cart.d, "right")
            elif next_section == "/":
                if cart.d in ["up", "down"]:
                    cart.d = turn(cart.d, "right")
                else:
                    cart.d = turn(cart.d, "left")

        carts = [cart for cart in carts if not cart.dead]
    print(carts)
