from functools import reduce

def part1() -> int:
    return [all([1 <= abs(d) <= 3 for d in a]) and (all([n < 0 for n in a]) or all([n > 0 for n in a])) for a in [list(map(lambda x: x[1] - x[0], zip(a, a[1:]))) for a in [list(map(int, x.split())) for x in open("./data/day2.txt").read().splitlines()]]].count(True)

def part2() -> int:
    return [(any([all([1 <= abs(d) <= 3 for d in a]) and (all([n < 0 for n in a]) or all([n > 0 for n in a])) for a in [list(map(lambda x: x[1] - x[0], zip(a, a[1:]))) for a in b]])) for b in [[a[:i] + a[i+1:] for i in range(len(a))] for a in [a for a in (list(map(int, x.split())) for x in open("./data/day2.txt").read().splitlines())]]].count(True)

def main() -> None:
    print(part2())

if __name__ == "__main__":
    main()