import itertools

def answer(num_buns, num_required):
    r = []
    combi = list(itertools.combinations(range(num_buns),num_required))
    total = len(combi)*num_required
    repeat_times = (num_buns - num_required) + 1

    new_combi = list(itertools.combinations(range(num_buns),repeat_times))
    
    for i in range(num_buns):
        r.append([])
    x = total/repeat_times

    for i in range(total/repeat_times):
        for j in new_combi[i]:
            r[j].append(i)
    return r