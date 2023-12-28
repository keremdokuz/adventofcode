import re

digit_texts_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
digit_texts_regex = f'{"|".join([digit_text for digit_text in digit_texts_map])}|[0-9]'


def isDigit(char: str) -> bool:
    return char in "1234567890"


def main() -> None:
    calibration_values_sum: int = 0

    with open("input.txt", "r") as input:
        for line in input:
            refurbished_line = line

            digit_text_pattern = re.compile(digit_texts_regex)

            if digit_text_pattern.search(refurbished_line) is not None:
                match = digit_text_pattern.search(refurbished_line).group(0)
                replacement = digit_texts_map.get(match, None)
                if replacement is not None:
                    refurbished_line = re.sub(match, str(replacement), refurbished_line, count=1)

            if re.search(f"(?s:.*)({digit_texts_regex})", refurbished_line) is not None:
                match = re.search(f"(?s:.*)({digit_texts_regex})", refurbished_line).group(1)
                print("refurbished:", refurbished_line, match, "neden")
                replacement = digit_texts_map.get(match, None)
                if replacement is not None:
                    refurbished_line = refurbished_line.replace(match, str(replacement))
                    print(refurbished_line, match, "neden2")

            digits = [char for char in refurbished_line if isDigit(char)]

            if len(digits) == 0:
                continue

            calibration_value: int = int(f"{digits[0]}{digits[-1]}")
            print(refurbished_line, calibration_value)
            print()

            calibration_values_sum += calibration_value

    print(calibration_values_sum)


if __name__ == "__main__":
    main()
