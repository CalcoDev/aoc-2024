def part1() -> int:
    d = open("./data/day4.txt", "r").read()
    lines = d.split("\n")
    
    dd = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            dd.append([x, y])
    s = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            for ddd in dd:
                isg = True
                for xx, k in enumerate("XMAS"):
                    xo = x + ddd[0] * xx
                    yo = y + ddd[1] * xx
                    if xo < 0 or yo < 0 or xo >= len(lines[y]) or yo >= len(lines):
                        isg = False
                        break
                    if lines[yo][xo] != k:
                        isg = False
                        break
                s += int(isg)
    return s

def part2() -> int:
    d = open("./data/day4.txt", "r").read()
    lines = d.split("\n")
    
    dd = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            dd.append([x, y])
    s = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != 'A':
                continue
            if x < 1 or y < 1 or x >= len(lines[y]) - 1 or y >= len(lines) - 1:
                continue
            d1 = (lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S') or (lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M')
            d2 = (lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S') or (lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M')
            s += d1 and d2
    return s

def main() -> None:
    print(part2())

if __name__ == "__main__":
    main()