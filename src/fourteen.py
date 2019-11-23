from src.tools import process


def run(input_file):
    for number in process(input_file):
        print(number)

        e1 = 0
        e2 = 1
        results = [3, 7]
        current = "37"

        while True:
            recipe1 = results[e1]
            recipe2 = results[e2]

            result = str(recipe1 + recipe2)
            current += result

            new = [int(c) for c in str(recipe1 + recipe2)]
            results.extend(new)

            if number in current:
                break
            else:
                current = current[-len(number) :]

            e1 = (recipe1 + e1 + 1) % len(results)
            e2 = (recipe2 + e2 + 1) % len(results)

        # if our number isn't the last part of the current result we need
        # to subtract one extra from how many recipes are before our number
        adjustment = 0 if current[-len(number) :] == number else 1
        print(len(results) - len(number) - adjustment)

