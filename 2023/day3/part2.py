import re


def isSymbol(char: str) -> bool:
    return char not in "1234567890" and char != "."


def main() -> None:
    grid: list[str] = []
    with open("input.txt", "r") as input:
        for line in input:
            grid.append(line.strip())

    x_dim = len(grid)
    y_dim = len(grid[0])

    star_positions = []
    for x in range(x_dim):
        for y in range(y_dim):
            if grid[x][y] == "*":
                star_positions.append({"x": x, "y": y, "gears": set()})

    for x, line in enumerate(grid):
        numbers = re.findall(r"\d+", line)

        start_index = 0
        prev_len = 0
        for number in numbers:
            start_index = line.find(number, start_index + prev_len)
            prev_len = len(number)

            for y in range(start_index, start_index + len(number)):
                # print(y, start_index, start_index + len(number))
                if y - 1 >= 0 and grid[x][y - 1] == "*":
                    for star_position in star_positions:
                        if star_position["x"] == x and star_position["y"] == (y - 1):
                            print(int(number))
                            star_position["gears"].add(int(number))
                if y + 1 < y_dim and grid[x][y + 1] == "*":
                    for star_position in star_positions:
                        if star_position["x"] == x and star_position["y"] == (y + 1):
                            print(int(number))
                            star_position["gears"].add(int(number))
                if x - 1 >= 0 and grid[x - 1][y] == "*":
                    for star_position in star_positions:
                        if star_position["x"] == (x - 1) and star_position["y"] == y:
                            print(int(number))
                            star_position["gears"].add(int(number))
                if x + 1 < x_dim and grid[x + 1][y] == "*":
                    for star_position in star_positions:
                        if star_position["x"] == (x + 1) and star_position["y"] == y:
                            print(int(number))
                            star_position["gears"].add(int(number))

                if y - 1 >= 0 and x - 1 >= 0 and grid[x - 1][y - 1] == "*":
                    for star_position in star_positions:
                        if star_position["x"] == (x - 1) and star_position["y"] == (y - 1):
                            print(int(number))
                            star_position["gears"].add(int(number))
                if y + 1 < y_dim and x - 1 >= 0 and grid[x - 1][y + 1] == "*":
                    for star_position in star_positions:
                        if star_position["x"] == (x - 1) and star_position["y"] == (y + 1):
                            print(int(number))
                            star_position["gears"].add(int(number))

                if y - 1 >= 0 and x + 1 < x_dim and grid[x + 1][y - 1] == "*":
                    for star_position in star_positions:
                        if star_position["x"] == (x + 1) and star_position["y"] == (y - 1):
                            print(int(number))
                            star_position["gears"].add(int(number))

                if x + 1 < x_dim and y + 1 < y_dim and grid[x + 1][y + 1] == "*":
                    for star_position in star_positions:
                        if star_position["x"] == (x + 1) and star_position["y"] == (y + 1):
                            print(int(number))
                            star_position["gears"].add(int(number))
    total = 0
    for star_position in star_positions:
        if len(star_position["gears"]) == 2:
            star_position_gear_list = list(star_position["gears"])
            print(star_position_gear_list)
            total += star_position_gear_list[0] * star_position_gear_list[1]
    print(total)


if __name__ == "__main__":
    main()
