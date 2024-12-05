from math import floor
from itertools import permutations

def part1() -> int:
    inp = open("./data/day5.txt", "r").read().split("\n\n")
    rinp = inp[0]
    uinp = inp[1]

    rules = []
    for l in rinp.split("\n"):
        v1, v2 = list(map(int, l.split("|")))
        rules.append((v1, v2))
    
    s = 0
    for l in [list(map(int, arr.split(","))) for arr in uinp.split("\n")]:
        idx = {}
        for i, n in enumerate(l):
            idx[n] = i
        good = True
        for a, b in rules:
            if a in l and b in l and not idx[a] < idx[b]:
                good = False
                break
        if good:
            s += l[floor(len(l) / 2)]
    
    return s

def part2() -> int:
    inp = open("./data/day5.txt", "r").read().split("\n\n")
    rinp = inp[0]
    uinp = inp[1]

    rules = []
    for l in rinp.split("\n"):
        v1, v2 = list(map(int, l.split("|")))
        rules.append((v1, v2))
    
    c = []
    for l in [list(map(int, arr.split(","))) for arr in uinp.split("\n")]:
        idx = {}
        for i, n in enumerate(l):
            idx[n] = i
        good = True
        for a, b in rules:
            if a in l and b in l and not idx[a] < idx[b]:
                good = False
                break
        if not good:
            c.append(l)
    
    s = 0
    for idx, p in enumerate(c):
        print(idx, " out of ", len(c))
        for l in permutations(p, len(p)):
            idx = {}
            for i, n in enumerate(l):
                idx[n] = i
            good = True
            for a, b in rules:
                if a in l and b in l and not idx[a] < idx[b]:
                    good = False
                    break
            if good:
                s += l[floor(len(l) / 2)]
                break
    
    return s

def part2_topology() -> int:
    inp = open("./data/day5.txt", "r").read().split("\n\n")
    rinp = inp[0]
    uinp = inp[1]

    rules = []
    rules_forward = {}
    for l in rinp.split("\n"):
        v1, v2 = list(map(int, l.split("|")))
        rules.append((v1, v2))
        if v1 not in rules_forward:
            rules_forward[v1] = set()
        rules_forward[v1].add(v2)
    
    c = []
    for l in [list(map(int, arr.split(","))) for arr in uinp.split("\n")]:
        idx = {}
        for i, n in enumerate(l):
            idx[n] = i
        good = True
        for a, b in rules:
            if a in l and b in l and not idx[a] < idx[b]:
                good = False
                break
        if not good:
            while True:
                is_sorted = True
                for i in range(len(l) - 1):
                    if (l[i+1], l[i]) in rules:
                        is_sorted = False
                        l[i], l[i+1] = l[i+1], l[i]
                if is_sorted:
                    c.append(l)
                    break
    s = 0
    for l in c:
        s += l[floor(len(l) / 2)]
    return s

def main() -> None:
    print(part2_topology())

if __name__ == "__main__":
    main()