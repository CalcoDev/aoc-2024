import pandas as pd

def part1() -> int:
    df = pd.read_csv("./data/day1.txt", delimiter="   ")
    df = pd.DataFrame({col: sorted(df[col]) for col in df.columns})
    d = 0
    for i in range(len(df["col1"])):
        d += abs(df["col2"][i] - df["col1"][i])
    return d

def part2() -> int:
    df = pd.read_csv("./data/day1.txt", delimiter="   ")
    df = pd.DataFrame({col: sorted(df[col]) for col in df.columns})
    vals = df["col2"].value_counts()
    sim = 0
    for i in range(len(df["col1"])):
        n = df["col1"][i]
        if n in vals:
            sim += n * vals[n]
    return sim

def main() -> None:
    print(part2())

if __name__ == "__main__":
    main()