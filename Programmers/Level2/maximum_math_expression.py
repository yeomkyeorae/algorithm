from itertools import permutations


def get_operator_perm(expression):
    op = []
    if "*" in expression:
        op.append("*")
    if "-" in expression:
        op.append("-")
    if "+" in expression:
        op.append("+")
    perm = list(permutations(op, len(op)))
    return perm


def extrand_ops(expression):
    expression_list = []

    str_num = ''
    for ex in expression:
        try:
            test = int(ex)
            str_num += ex
        except ValueError:
            expression_list.append(int(str_num))
            str_num = ''
            expression_list.append(ex)
    expression_list.append(int(str_num))

    return expression_list


def get_value(expression, perm):
    expression_list = extrand_ops(expression)

    for p in perm:

        new_expression_list = []
        do_it = False
        for expression in expression_list:
            if expression in perm:
                if expression == p:
                    do_it = True
                else:
                    new_expression_list.append(expression)
            else:
                if do_it:
                    if p == '+':
                        new_expression_list[-1] = new_expression_list[-1] + expression
                    elif p == '-':
                        new_expression_list[-1] = new_expression_list[-1] - expression
                    elif p == '*':
                        new_expression_list[-1] = new_expression_list[-1] * expression
                    do_it = False
                else:
                    new_expression_list.append(expression)
        expression_list = new_expression_list

    return expression_list[0]


def solution(expression):
    answer = 0
    perms = get_operator_perm(expression)
    for perm in perms:
        value = abs(get_value(expression, perm))
        if answer < value:
            answer = value

    return answer
