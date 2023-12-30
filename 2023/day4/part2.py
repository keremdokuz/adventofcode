def main() -> None:
    """
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    """
    cards_numbers: dict[str, tuple[list[int], list[int]]] = {}
    cards_instances: dict[str, int] = {}
    with open("input.txt", "r") as input:
        for line in input:
            content = line.split(":")
            card_number = content[0].split()[1]
            numbers = content[1].split("|")
            cards_numbers[card_number] = (
                [int(winning_number) for winning_number in numbers[0].split()],
                [int(our_number) for our_number in numbers[1].split()],
            )
            cards_instances[card_number] = 1

    for card_number, card_info in cards_numbers.items():
        winning_numbers = card_info[0]
        our_numbers = card_info[1]

        matching_count = 0
        for winning_number in winning_numbers:
            if winning_number in our_numbers:
                matching_count += 1

        card_idx = int(card_number) + 1
        while matching_count > 0:
            print(card_idx, matching_count)
            if f"{card_idx}" not in cards_instances:
                break
            cards_instances[f"{card_idx}"] += cards_instances[card_number]
            card_idx += 1
            matching_count -= 1

    print(cards_instances)
    print(sum(instances for instances in cards_instances.values()))


if __name__ == "__main__":
    main()
