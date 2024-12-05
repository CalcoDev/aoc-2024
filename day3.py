import re
from functools import reduce

def part1() -> int:
    inp = open("./data/day3.txt", "r").read()
    p = r"mul\(\d{1,3},\d{1,3}\)"
    occ = re.findall(p, inp)
    return sum([int(o.split(",")[0].split("(")[1]) * int(o.split(",")[1].split(")")[0]) for o in occ])

def part2() -> int:
    inp = open("./data/day3.txt", "r").read()
    p = r"(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
    occ = re.findall(p, inp)
    state = {"t": True}
    t = reduce(lambda acc, x: ({"do(": lambda: state.update(t=True) or acc, "don": lambda: state.update(t=False) or acc, "mul": lambda: acc + [x] if state["t"] else acc }[x[:3]]()), occ, [])
    return sum([int(o.split(",")[0].split("(")[1]) * int(o.split(",")[1].split(")")[0]) for o in t])


def part1_unreadable() -> int:
    return sum([int(o.split(",")[0].split("(")[1]) * int(o.split(",")[1].split(")")[0]) for o in re.findall(r"mul\(\d{1,3},\d{1,3}\)", open("./data/day3.txt", "r").read())])

def part2_unreadable() -> int:
    state = {"t": True}
    return sum([int(o.split(",")[0].split("(")[1]) * int(o.split(",")[1].split(")")[0]) for o in reduce(lambda acc, x: ({"do(": lambda: state.update(t=True) or acc, "don": lambda: state.update(t=False) or acc, "mul": lambda: acc + [x] if state["t"] else acc }[x[:3]]()), re.findall(r"(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", open("./data/day3.txt", "r").read()), [])])

def part2_unreadable_gippity() -> int:
    return sum(int(o.split(",")[0].split("(")[1]) * int(o.split(",")[1].split(")")[0]) for o in reduce(lambda acc, x: (acc[0] + [x] if acc[1] and x[:3] == "mul" else acc[0], True if x[:3] == "do(" else False if x[:3] == "don" else acc[1]), re.findall(r"(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", open("./data/day3.txt", "r").read()), ([], True))[0])

def main() -> None:
    print(part2_unreadable_gippity())

if __name__ == "__main__":
    main()