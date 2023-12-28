cube_limits = {"red": 12, "green": 13, "blue": 14}


def main() -> None:
    total = 0
    with open("input2.txt", "r") as input:
        for line in input:
            splitted_game_info = line.split(":")

            game_info = splitted_game_info[0]  # Game 1
            current_game_number = int(game_info.split(" ")[1])

            game_content = splitted_game_info[1].strip()  # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            games = game_content.split("; ")

            valid_game = True

            for game in games:
                cube_infos = game.split(", ")

                for cube_info in cube_infos:
                    splitted_info = cube_info.split(" ")
                    count, color = int(splitted_info[0]), splitted_info[1]
                    supposed_count = cube_limits.get(color, None)

                    if supposed_count is not None and count > supposed_count:
                        valid_game = False

            if valid_game:
                print(current_game_number)
                total += current_game_number
    print(total)

if __name__ == "__main__":
    main()
