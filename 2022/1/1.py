from pprint import pprint


def parse_input():

    elfInventories = []

    oneElf = []

    with open('input','r') as f:
        for line in f.readlines():
            line = line.strip()

            # print("line:"+line)

            if line == '':
                elfInventories.append(oneElf)
                oneElf=[]
            else:
                oneElf.append(int(line))

    return elfInventories

elfInventories = parse_input()

pprint(elfInventories)

elfInventories_summed = [sum(inv) for inv in elfInventories]

pprint(elfInventories_summed)

largest = max(elfInventories_summed)

print("largest="+str(largest))

largest_3 = sorted(elfInventories_summed)[::-1][0:3]

pprint(largest_3)

largest_3_summed = sum(largest_3)

print(largest_3_summed)