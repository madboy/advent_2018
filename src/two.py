from src.tools import process


def run(input_file):
    twos = 0
    threes = 0
    box_ids = []

    for line in process(input_file):
        box_id = line.strip()
        box_ids.append(box_id)
        two_counted = False
        three_counted = False
        for letter in box_id:
            c = box_id.count(letter)
            if c == 2 and not two_counted:
                twos += 1
                two_counted = True

            if c == 3 and not three_counted:
                threes += 1
                three_counted = True

    print(twos * threes)

    for i, box_id in enumerate(box_ids):
        for box_id2 in box_ids[i + 1 :]:
            diff = 0
            index = -1
            for i in range(len(box_id)):
                if box_id[i] != box_id2[i]:
                    index = i
                    diff += 1
            if diff == 1:
                print("{}{}".format(box_id[0:index], box_id[index + 1 :],))
