import re   # https://regex101.com/


def parse_instructions(input_file):
    instructions = list()
    with open(input_file, 'r') as file:
        for line in file:
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


def run_boot_code_pt1(boot_code):
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
    boot_code = parse_instructions(input_file)
    return run_boot_code_pt1(boot_code)


def test_boot_code_for_loop(boot_code) -> list:
    global accumulator, stack_pointer
    accumulator = int(0)
    stack_pointer = int(0)
    visited_jmp_instructions = set()
    while stack_pointer < len(boot_code):  # loop till bottom
        instruction = boot_code[stack_pointer]
        if instruction[0] == 'jmp':
            if stack_pointer not in visited_jmp_instructions:
                visited_jmp_instructions.add(stack_pointer)
            else:
                return [1, accumulator]  # visit a JMP twice -> infinite loop
        op_vtable[instruction[0]](instruction[1])
    return [0, accumulator]  # success, return no error code and accumulator


def modify_boot_code(input_file):
    with open(input_file):
        boot_code = parse_instructions(input_file)
        changeable_set = {'jmp', 'nop'}
        for instruction_idx in range(len(boot_code)):
            if boot_code[instruction_idx][0] in changeable_set:  # try replacing OP here
                boot_code[instruction_idx][0] = changeable_set.difference({boot_code[instruction_idx][0]}).pop()  
                [error_code, acc] = test_boot_code_for_loop(boot_code)
                if error_code == 0:  # we found a solution
                    return [error_code, acc]
                else:  # reset instruction
                    boot_code[instruction_idx][0] = changeable_set.difference({boot_code[instruction_idx][0]}).pop()  
        return [1, acc]  # didnt find a solution
