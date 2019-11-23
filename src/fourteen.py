from src.tools import process


def run(input_file):
    for number in process(input_file):
        number = int(number)
        print(number)

        e1 = 0
        e2 = 1
        results = [3, 7]

        while len(results) < number + 10:
            recipe1 = results[e1]
            recipe2 = results[e2]

            new = [int(c) for c in str(recipe1 + recipe2)]
            results.extend(new)

            e1 = (recipe1 + e1 + 1) % len(results)
            e2 = (recipe2 + e2 + 1) % len(results)

        print("".join([str(n) for n in results[number : number + 10]]))
