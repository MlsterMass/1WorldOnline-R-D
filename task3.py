import re


class Calculator:
    _val1 = 0
    _val2 = 0

    def sum(self, _val1, _val2):
        result = _val1 + _val2
        return result

    def difference(self, _val1, _val2):
        result = _val1 - _val2
        return result

    def multiplication(self, _val1, _val2):
        result = _val1 * _val2
        return result

    def division(self, _val1, _val2):
        result = _val1 / _val2
        return result

    def degree(self, _val1, _val2):
        result = _val1 ** _val2
        return result

    def sqrt(self, _val1):
        result = _val1 ** 0.5
        return result

    def save_to_memory(self, val):
        with open('memory.txt', 'a') as f:
            f.write(val + ',')

    def clear_memory(self):
        open('memory.txt', 'w').close()

    def take_from_memory(self, index):
        try:
            with open('memory.txt', 'r') as f:
                d = f.read()
                data = d.split(',')
                return data[index]
        except (IndexError, TypeError) as err:
            print("Memory is empty")
            return err

    def save_result_to_memory(self, res):
        res_save = input('Save result to memory? ')
        if re.fullmatch('M', res_save):
            calc.save_to_memory(str(res))
            print('Result saved to memory')


exp = input()
calc = Calculator()

if re.fullmatch(r'[-]?[\d]+[+]?[\d]+', exp):
    val1 = int(exp.split('+')[0])
    val2 = int(exp.split('+')[1])
    res = calc.sum(val1, val2)
    print(res)
    calc.save_result_to_memory(res)

if re.fullmatch(r'[-]?[\d]+[-]?[\d]+', exp):
    if exp[0] == '-':
        val1 = int('-' + exp[1:].split('-')[0])
        val2 = int(exp[1:].split('-')[1])
        res = calc.difference(val1, val2)
        print(res)
        calc.save_result_to_memory(res)
    else:
        val1 = int(exp.split('-')[0])
        val2 = int(exp.split('-')[1])
        res = calc.difference(val1, val2)
        print(res)
        calc.save_result_to_memory(res)
if re.fullmatch(r'[-]?[\d]+[*]?[\d]+', exp):
    val1 = int(exp.split('*')[0])
    val2 = int(exp.split('*')[1])
    res = calc.multiplication(val1, val2)
    print(res)
    calc.save_result_to_memory(res)
if re.fullmatch(r'[-]?[\d]+[/]?[\d]+', exp):
    val1 = int(exp.split('/')[0])
    val2 = int(exp.split('/')[1])
    res = calc.division(val1, val2)
    print(res)
    calc.save_result_to_memory(res)
if re.fullmatch(r'[-]?([\d]+)\*\*[\d]+', exp):
    val1 = int(exp.split('**')[0])
    val2 = int(exp.split('**')[-1])
    res = calc.degree(val1, val2)
    print(res)
    calc.save_result_to_memory(res)
if re.fullmatch(r'\^\-?\d*', exp):
    val = int(exp.split('^')[1])
    res = calc.sqrt(val)
    print(res)
    calc.save_result_to_memory(res)

# Work with memory
if re.fullmatch(r'M=[-]?\d*', exp):
    val = exp.split('=')[-1]
    calc.save_to_memory(val)

if re.fullmatch(r'MC', exp):
    calc.clear_memory()
    print('Memory cleared')

if re.fullmatch(r'M-\d*', exp):
    val = int(exp.split('-')[-1])
    res = calc.take_from_memory(val)
    print(res)


# Memory functions
def memory_sum_int():
    i = int(exp.split('-')[1][0])
    mem = int(calc.take_from_memory(i))
    val = int(exp.split('+')[-1])
    res = calc.sum(mem, val)
    print(res)
    calc.save_result_to_memory(res)


def memory_difference_int():
    i = int(exp.split('-')[1][0])
    mem = int(calc.take_from_memory(i))
    val = int(exp.split('-')[-1])
    res = calc.difference(mem, val)
    print(res)
    calc.save_result_to_memory(res)


def memory_multiplication_int():
    i = int(exp.split('-')[1][0])
    mem = int(calc.take_from_memory(i))
    val = int(exp.split('*')[-1])
    res = calc.multiplication(mem, val)
    print(res)
    calc.save_result_to_memory(res)


def memory_division_int():
    i = int(exp.split('-')[1][0])
    mem = int(calc.take_from_memory(i))
    val = int(exp.split('/')[-1])
    res = calc.division(mem, val)
    print(res)
    calc.save_result_to_memory(res)


def memory_degree_int():
    i = int(exp.split('-')[1][0])
    mem = int(calc.take_from_memory(i))
    val = int(exp.split('**')[-1])
    res = calc.degree(mem, val)
    print(res)
    calc.save_result_to_memory(res)


def memory_sqrt():
    i = int(exp.split('^')[1][-1])
    mem = int(calc.take_from_memory(i))
    res = calc.sqrt(mem)
    print(res)
    calc.save_result_to_memory(res)


# Memory operations M operand int

if re.fullmatch(r'M-\d*[+]?[\d]+', exp):
    try:
        memory_sum_int()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'M-\d*[+]?[\d]+', exp):
            memory_sum_int()
if re.fullmatch(r'M-\d*[-]?[\d]+', exp):
    try:
        memory_difference_int()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'M-\d*[-]?[\d]+', exp):
            memory_difference_int()
if re.fullmatch(r'M-\d*[*]?[\d]+', exp):
    try:
        memory_multiplication_int()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'M-\d*[*]?[\d]+', exp):
            memory_multiplication_int()
if re.fullmatch(r'M-\d*[/]?[\d]+', exp):
    try:
        memory_division_int()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'M-\d*[/]?[\d]+', exp):
            memory_division_int()
if re.fullmatch(r'M-\d*\**[\d]+', exp):
    try:
        memory_degree_int()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'M-\d*\**[\d]+', exp):
            memory_degree_int()
if re.fullmatch(r'\^\w\-\d+', exp):
    try:
        memory_sqrt()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'\^\w\-\d+', exp):
            memory_sqrt()


# Memory functions for int operand M

def int_sum_memory():
    i = int(exp.split('-')[1][0])
    mem = int(calc.take_from_memory(i))
    val = int(exp.split('+')[0])
    res = calc.sum(val, mem)
    print(res)
    calc.save_result_to_memory(res)


def int_difference_memory():
    i = int(exp.split('-')[2])
    mem = int(calc.take_from_memory(i))
    val = int(exp.split('-')[0])
    res = calc.difference(val, mem)
    print(res)
    calc.save_result_to_memory(res)


def int_multiplication_memory():
    i = int(exp.split('-')[-1])
    mem = int(calc.take_from_memory(i))
    val = int(exp.split('*')[0])
    res = calc.multiplication(val, mem)
    print(res)
    calc.save_result_to_memory(res)


def int_division_memory():
    i = int(exp.split('-')[-1])
    mem = int(calc.take_from_memory(i))
    val = int(exp.split('/')[0])
    res = calc.division(val, mem)
    print(res)
    calc.save_result_to_memory(res)


def int_degree_memory():
    i = int(exp.split('-')[-1])
    mem = int(calc.take_from_memory(i))
    val = int(exp.split('**')[0])
    res = calc.degree(val, mem)
    print(res)
    calc.save_result_to_memory(res)


# Memory operations int operand M

if re.fullmatch(r'[-]?\d+\+M-\d+', exp):
    try:
        int_sum_memory()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'[-]?\d+\+M-\d+', exp):
            int_sum_memory()
if re.fullmatch(r'[-]?\d+\-M-\d+', exp):
    try:
        int_difference_memory()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'[-]?\d+\-M-\d+', exp):
            int_difference_memory()
if re.fullmatch(r'[-]?\d+[*]M-\d+', exp):
    try:
        int_multiplication_memory()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'[-]?\d+[*]M-\d+', exp):
            int_multiplication_memory()
if re.fullmatch(r'[-]?\d+[/]M-\d+', exp):
    try:
        int_division_memory()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'[-]?\d+[/]M-\d+', exp):
            int_division_memory()
if re.fullmatch(r'[-]?\d+\**M-\d+', exp):
    try:
        int_degree_memory()
    except (ValueError, TypeError, IndexError) as err:
        exp = input()
        if re.fullmatch(r'[-]?\d+\**M-\d+', exp):
            int_degree_memory()
