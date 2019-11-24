from src.tools import process


def new_recipe(e1, e2, results):
    recipe1 = results[e1]
    recipe2 = results[e2]

    new = [int(c) for c in str(recipe1 + recipe2)]
    results.extend(new)

    e1 = (recipe1 + e1 + 1) % len(results)
    e2 = (recipe2 + e2 + 1) % len(results)
    return e1, e2


def part1(number, e1, e2, results):
    number = int(number)
    print(number)

    # e1 = 0
    # e2 = 1
    # results = [3, 7]

    while len(results) < number + 10:
        e1, e2 = new_recipe(e1, e2, results)

    print("".join([str(n) for n in results[number : number + 10]]))


def part2(number, e1, e2, results):
    number = [int(c) for c in number]
    print(number)

    # e1 = 0
    # e2 = 1
    # results = [3, 7]

    while True:
        e1, e2 = new_recipe(e1, e2, results)

        if (
            number == results[-len(number) :]
            or number == results[-(len(number) + 1) : -1]
        ):
            break

    # if our number isn't the last part of the current result we need
    # to subtract one extra from how many recipes are before our number
    adjustment = 0 if results[-len(number) :] == number else 1
    print(len(results) - len(number) - adjustment)


def run(input_file):
    for number in process(input_file):
        part1(number, e1=0, e2=1, results=[3, 7])
        part2(number, e1=0, e2=1, results=[3, 7])
