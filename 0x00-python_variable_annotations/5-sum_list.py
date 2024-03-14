#!/usr/bin/env python3

def sum_list(input_list: list[float]) -> float:
    '''sum a list of float numbers'''
    result = 0
    for num in input_list:
        result += num
    return float(result)
