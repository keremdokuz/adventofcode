import re


def isSymbol(char: str) -> bool:
    return char not in "1234567890" and char != "."

def main() -> None:
    grid: list[str] = []
    with open("input.txt", "r") as input:
        for line in input:
            grid.append(line.strip())

    print(grid)
    x_dim = len(grid)
    y_dim = len(grid[0])
    total = 0

    for x, line in enumerate(grid):
        numbers = re.findall(r"\d+", line)
        print(numbers)

        start_index = 0
        prev_len = 0
        for number in numbers:
            start_index = line.find(number, start_index + prev_len)
            prev_len = len(number)

            for y in range(start_index, start_index + len(number)):
                # print(y, start_index, start_index + len(number))
                if y - 1 >= 0:
                    if isSymbol(grid[x][y - 1]):
                        total += int(number)
                        print(int(number))
                        break
                if y + 1 < y_dim:
                    if isSymbol(grid[x][y + 1]):
                        total += int(number)
                        print(int(number))
                        break
                if x - 1 >= 0:
                    if isSymbol(grid[x - 1][y]):
                        total += int(number)
                        print(int(number))
                        break
                if x + 1 < x_dim:
                    if isSymbol(grid[x + 1][y]):
                        total += int(number)
                        print(int(number))
                        break

                if y - 1 >= 0 and x - 1 >= 0:
                    if isSymbol(grid[x - 1][y - 1]):
                        total += int(number)
                        print(int(number))
                        break
                if y + 1 < y_dim and x - 1 >= 0:
                    if isSymbol(grid[x - 1][y + 1]):
                        total += int(number)
                        print(int(number))
                        break
                if y - 1 >= 0 and x + 1 < x_dim:
                    if isSymbol(grid[x + 1][y - 1]):
                        total += int(number)
                        print(int(number))
                        break
                if x + 1 < x_dim and y + 1 < y_dim:
                    if isSymbol(grid[x + 1][y + 1]):
                        total += int(number)
                        print(int(number))
                        break
    print(total)
if __name__ == "__main__":
    main()
