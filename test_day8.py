from Day8_HandheldHalting import parse_instructions, run_part1, part2_modify_boot_code

test_parse_result = [["nop", 0], ["acc", 1], ["jmp", 4], ["acc", 3], ["jmp", -3], ["acc", -99], ["acc", 1], ["jmp", -4], ["acc", 6]]

def test_parser_part1():
    input_file = "Day8_simple_input.txt"
    boot_code = parse_instructions(input_file)
    assert boot_code == test_parse_result


def test_part1():
    input_file = "Day8_input.txt"
    last_instruction_line = run_part1(input_file)
    assert last_instruction_line == 1521


def test_part2():
    input_file = "Day8_input.txt"
    [error_code, accumulator_value] = part2_modify_boot_code(input_file)
    assert [error_code, accumulator_value] == [0, 1016]
