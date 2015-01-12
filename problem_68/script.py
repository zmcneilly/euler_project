#!env/bin/python3

PVALS = range(1, 11)

def tup_to_int(first, second, third, fourth, fifth):
    result = ''.join([str(_i) for _i in first])
    result += ''.join([str(_i) for _i in second])
    result += ''.join([str(_i) for _i in third])
    result += ''.join([str(_i) for _i in fourth])
    result += ''.join([str(_i) for _i in fifth])
    return int(result)


def find_first_3gon():
    for _i in PVALS:
        for _j in PVALS:
            if _i == _j:
                continue
            for _k in PVALS:
                if _k in (_i, _j):
                    continue
                yield (_i, _j, _k)


def find_sec_3gon(pvals, max_digit, total, first):
    _j = first[2]
    for _i in pvals:
        if _i <= max_digit:
            continue
        _k = total - _j - _i
        if _k in pvals and _k != _i:
            yield (_i, _j, _k)


if __name__ == "__main__":
    max_solution = 0
    for first in find_first_3gon():
        pvals = [_i for _i in PVALS if _i not in first]
        total = sum(first)
        for second in find_sec_3gon(pvals, first[0], total, first):
            pvals_2 = [_i for _i in pvals if _i not in second]
            for third in find_sec_3gon(pvals_2, first[0], total, second):
                pvals_3 = [_i for _i in pvals_2 if _i not in third]
                for fourth in find_sec_3gon(pvals_3, first[0], total, third):
                    pvals_4 = [_i for _i in pvals_3 if _i not in fourth][0]
                    fifth = (pvals_4, fourth[2], first[1])
                    if pvals_4 > first[0] and sum(fifth) == total:
                        result = tup_to_int(first, second, third, fourth,
                                            fifth)
                        if result > max_solution and len(str(result)) == 16:
                            max_solution = result
    print(max_solution)
