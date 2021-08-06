import re


#  def instruction = [pos opcode arg_list]

def parse_instructions(raw_instructions):
    instructions = list()
    for line in raw_instructions:
        op_code, arg1 = re.match('[]{3} {2}/d?', line)
        instructions.append(op_code, arg1)
    return instructions


# input the current arc, write result to ACC
def op_ACC(pos, acc, arg) -> int:
    acc += arg
    return acc


# input the instruction location and argument, write result to ACC
def op_JMP(pos, acc, arg) -> int:
    pos += arg
    return pos


# Noop increments ACC by one
def op_NO_OP(pos, acc, arg) -> int:
    return (acc+1)


op_vtable = {
    'acc': op_ACC,
    'jmp': op_JMP,
    'nop': op_NO_OP,
}


def run_boot_code(boot_code):
    global accumulator, stack_pointer
    accumulator = 0
    stack_pointer = 0
    visited_instructions = set()
    while True:  # infinite loop
        if stack_pointer not in visited_instructions:
            visited_instructions.add(stack_pointer)
            instruction = boot_code[stack_pointer]
            op_vtable[instruction[0]](stack_pointer, accumulator, instruction[1:])
        else:
            return accumulator


def run_part1(input_file):
    with open(input_file, 'r') as file:
        boot_code = parse_instructions(file)
    output_instruction = run_boot_code(boot_code)