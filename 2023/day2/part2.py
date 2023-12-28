def multiply_all(list_to_mult: list[int]) -> int:
    result = 1
    for num in list_to_mult:
        result *= num
    return result


def main() -> None:
    with open("input2.txt", "r") as input:
        total = 0
        for line in input:
            min_cube_limits = {"red": 0, "green": 0, "blue": 0}
            splitted_game_info = line.split(":")

            game_content = splitted_game_info[1].strip()  # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            games = game_content.split("; ")

            for game in games:
                cube_infos = game.split(", ")

                for cube_info in cube_infos:
                    splitted_info = cube_info.split(" ")
                    count, color = int(splitted_info[0]), splitted_info[1]
                    current_min_count = min_cube_limits.get(color, None)

                    if current_min_count is not None and count > current_min_count:
                        min_cube_limits[color] = count
            game_power = multiply_all([min_cube_limits[color] for color in min_cube_limits if min_cube_limits[color] != 0])
            total += game_power
    print(total)


if __name__ == "__main__":
    main()
