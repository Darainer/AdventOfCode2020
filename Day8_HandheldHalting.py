import re   # https://regex101.com/


def parse_instructions(raw_instructions):
    instructions = list()
    for line in raw_instructions:
        [op_code, arg1] = re.split(r" ", line.strip())
        instructions.append([op_code, int(arg1)])
    return instructions


# input the current arc, write result to ACC
def op_ACC(arg):
    global accumulator, stack_pointer
    accumulator += arg
    stack_pointer += 1


# input the instruction location and argument, write result to pos
def op_JMP(arg):
    global stack_pointer
    stack_pointer += arg


# Noop increments ACC by one
def op_NO_OP(arg):
    global stack_pointer
    stack_pointer += 1


op_vtable = {
    'acc': op_ACC,
    'jmp': op_JMP,
    'nop': op_NO_OP,
}


def run_boot_code(boot_code):
    global accumulator, stack_pointer
    accumulator = int(0)
    stack_pointer = int(0)
    visited_instructions = set()
    while True:  # infinite loop
        if stack_pointer not in visited_instructions:
            visited_instructions.add(stack_pointer)
            instruction = boot_code[stack_pointer]
            op_vtable[instruction[0]](instruction[1])
        else:
            return accumulator


def run_part1(input_file):
    with open(input_file, 'r') as file:
        boot_code = parse_instructions(file)
    return run_boot_code(boot_code)
