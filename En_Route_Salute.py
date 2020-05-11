
def solution(s):

    right_arrow = '>'
    left_arrow = '<'
    empty_string = '-'

    input_list = list(s)

    arrow_list = [elm for elm in input_list if elm is not empty_string]

    arrow_dict = {'right': [], 'left': []}

    # Store positions of right arrows and left ones
    for i, elm in enumerate(arrow_list):

        if elm == right_arrow:
            arrow_dict['right'].append(i)

        if elm == left_arrow:
            arrow_dict['left'].append(i)

    r_encount = 0
    l_encount = 0

    for i, r_elm in enumerate(arrow_dict['right']):
        for j, l_elm in enumerate(arrow_dict['left']):
            if r_elm < l_elm:
                r_encount += 1

    for i, l_elm in enumerate(arrow_dict['left']):
        for j, r_elm in enumerate(arrow_dict['right']):
            if r_elm < l_elm:
                l_encount += 1

    return r_encount + l_encount