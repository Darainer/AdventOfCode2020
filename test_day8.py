from Day8_HandheldHalting import run_part1, parse_instructions

test_parse_result = [["nop", 0], ["acc", 1], ["jmp", 4], ["acc", 3], ["jmp", -3], ["acc", -99],["acc", 1], ["jmp", -4], ["acc", 6]]


def test_parser_part1():
    input_file = "Day8_simple_input.txt"
    with open(input_file, 'r') as file:
        boot_code = parse_instructions(file)
    assert boot_code == test_parse_result


def test_part1():
    input_file = "Day8_input.txt"
    last_instruction_line = run_part1(input_file)
    assert last_instruction_line == 268