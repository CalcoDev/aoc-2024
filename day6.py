from math import floor
from itertools import permutations, cycle, takewhile, chain
import time

def part1() -> int:
    inp = open("./data/day6.txt", "r").read()
    map_size = (len(inp.split("\n")), len(inp.split('\n')[0]))
    start = (inp.split('\n')[(inp.find('^') // len(inp.split("\n")[0])) - 1].find('^'), inp.find('^') // len(inp.split("\n")[0]) - 1)
    blockers = list(chain(*filter(lambda a: len(a) > 0, [list(filter(lambda i: i != False, [(col_idx, row_idx) if col == '#' else False for col_idx, col in enumerate(row)])) for row_idx, row in enumerate(inp.split("\n"))])))
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    move = lambda start, direction: (
        (x, y) for x, y in takewhile(
                            lambda p: -1 <= p[0] <= map_size[0] and -1 <= p[1] <= map_size[1] and (p[0], p[1]) not in blockers,
                            ([start[0] + direction[0] * i, start[1] + direction[1] * i]
                            for i in takewhile(lambda i: -1 <= start[0] + direction[0] * i <= map_size[0] and -1 <= start[1] + direction[1] * i <= map_size[1] and [start[0] + direction[0] * i, start[1] + direction[1] * i] not in blockers, range(max(map_size[0], map_size[1]) + 1)))
        )
    )
    
    cpos = [start]
    pdir = directions[0]
    test = [cpos := list(move(cpos[-1], pdir := direction)) for direction in takewhile(lambda p: -1 <= cpos[-1][0] + pdir[0] <= map_size[0] and -1 <= cpos[-1][1] + pdir[1] <= map_size[1], cycle(directions))]
    t = ([(x, y) for x, y in chain(*test)])
    
    return len(set(t)) - 1

def part1_unreadable() -> int:
    test = (lambda pdir, start, map_size, blockers: ([start := list((lambda start, direction: ((x, y) for x, y in takewhile(lambda p: -1 <= p[0] <= map_size[0] and -1 <= p[1] <= map_size[1] and (p[0], p[1]) not in blockers, ([start[0] + direction[0] * i, start[1] + direction[1] * i] for i in takewhile(lambda i: -1 <= start[0] + direction[0] * i <= map_size[0] and -1 <= start[1] + direction[1] * i <= map_size[1] and [start[0] + direction[0] * i, start[1] + direction[1] * i] not in blockers, range(max(map_size[0], map_size[1]) + 1))))))(start[-1], pdir := direction)) for direction in takewhile(lambda p: -1 <= start[-1][0] + pdir[0] <= map_size[0] and -1 <= start[-1][1] + pdir[1] <= map_size[1], cycle([[0, -1], [1, 0], [0, 1], [-1, 0]]))]))([-1, 0], [(open("./data/day6.txt", "r").read().split('\n')[(open("./data/day6.txt", "r").read().find('^') // len(open("./data/day6.txt", "r").read().split("\n")[0])) - 1].find('^'), open("./data/day6.txt", "r").read().find('^') // len(open("./data/day6.txt", "r").read().split("\n")[0]) - 1)], [len(open("./data/day6.txt", "r").read().split("\n")), len(open("./data/day6.txt", "r").read().split('\n')[0])] , list(chain(*filter(lambda a: len(a) > 0, [list(filter(lambda i: i != False, [(col_idx, row_idx) if col == '#' else False for col_idx, col in enumerate(row)])) for row_idx, row in enumerate(open("./data/day6.txt", "r").read().split("\n"))]))))
    return len(set([(x, y) for x, y in chain(*test)])) - 1

def part2() -> int:
    inp = open("./data/day6.txt", "r").read()
    map_size = (len(inp.split("\n")), len(inp.split('\n')[0]))
    start = (inp.split('\n')[(inp.find('^') // len(inp.split("\n")[0])) - 1].find('^'), inp.find('^') // len(inp.split("\n")[0]) - 1)
    blockers = list(chain(*filter(lambda a: len(a) > 0, [list(filter(lambda i: i != False, [(col_idx, row_idx) if col == '#' else False for col_idx, col in enumerate(row)])) for row_idx, row in enumerate(inp.split("\n"))])))
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    move = lambda start, direction: (
        (x, y) for x, y in takewhile(
                            lambda p: -1 <= p[0] <= map_size[0] and -1 <= p[1] <= map_size[1] and (p[0], p[1]) not in blockers,
                            ([start[0] + direction[0] * i, start[1] + direction[1] * i]
                            for i in takewhile(lambda i: -1 <= start[0] + direction[0] * i <= map_size[0] and -1 <= start[1] + direction[1] * i <= map_size[1] and [start[0] + direction[0] * i, start[1] + direction[1] * i] not in blockers, range(max(map_size[0], map_size[1]) + 1)))
        )
    )
    
    pcnt = 0
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            if (x, y) in blockers:
                continue
            if x == start[0] and y == start[1]:
                continue
            # print("Checking (", x, " ", y, ").")
            blockers.append((x, y))
            start_time = time.time()
    
            cpos = [start]
            pdir = directions[0]
            test = [cpos := list(move(cpos[-1], pdir := direction)) for direction in takewhile(lambda p: time.time() - start_time < 1 and -1 <= cpos[-1][0] + pdir[0] <= map_size[0] and -1 <= cpos[-1][1] + pdir[1] <= map_size[1], cycle(directions))]
            if time.time() - start_time > 0.5:
                # print("(", x, " ", y, ") was loop.")
                pcnt += 1
            blockers.remove((x, y))
    
    return pcnt

def main() -> None:
    print(part2())

if __name__ == "__main__":
    main()