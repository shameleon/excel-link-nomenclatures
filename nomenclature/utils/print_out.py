#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
printout.py for colorful stdout or stderr output

Usage:
    from utils import printout as po
    po.as_title2("Hello")

Description:
    colored and customizable output
    - output to terminal stdout and stderr.
    - asks for terminal user input
"""
__authors__ = ['jmouaike']

import sys

"""Color code
https://talyian.github.io/ansicolors/ """
COL_RESET = '\x1b[0m'
COL_ORANGE = '\x1b[38:5:208m'
COL_TURQU = '\x1b[38;5;45m'
COL_FTLIN = '\x1b[48:5:208m'
COL_GRNBLK = '\x1b[1;32;40m'
COL_GRNWHI = '\x1b[2;32;47m'
COL_BLUWHI = '\x1b[2;34;47m'
COL_BLUCYA = '\x1b[1;34;42m'
COL_BLUWHI = '\x1b[1;34;47m'
COL_BLURED = '\x1b[2;34;41m'
COL_REDWHI = '\x1b[1;31;47m'
COL_ERR = '	\x1b[38;5;9m'
COL_QUERY = '\x1b[2;37;40m'
COL_ASKKM = '\x1b[2;34;43m'


def printout_title(level: int, mssg: str):
    """Project name then Title1 printed with
    colorful central padding : ^80
    """
    color = {1: COL_BLUWHI, 2: COL_TURQU, 3: COL_BLUWHI}
    if level == 1:
        project_name = 'Datascience X Logistic Regression'
        print(f'\n{COL_FTLIN}{project_name:_^80}{COL_RESET}')
    print(f'{color[level]}{mssg: ^80}{COL_RESET}\n')


def as_title(mssg: str):
    printout_title(1, mssg)


def as_title2(mssg: str):
    printout_title(2, mssg)


def as_title3(mssg: str):
    printout_title(3, mssg)


def printout_one_line(color, mssg: str):
    """ colored one-line printed to stdout"""
    print(f'{color}{mssg}{COL_RESET}\n')


def as_result(mssg: str):
    printout_one_line(COL_ORANGE, mssg)


def as_comment(mssg: str):
    printout_one_line(COL_GRNBLK, mssg)


def as_status(mssg: str):
    printout_one_line(COL_FTLIN, mssg)


def as_check(mssg: str):
    print("✅", f'{COL_BLUWHI}{mssg}{COL_RESET}\n')


def as_cross(mssg: str):
    print("❌", f'{COL_REDWHI}{mssg}{COL_RESET}\n')


def as_error(mssg: str):
    print(f'{COL_ERR}{mssg}{COL_RESET}', file=sys.stderr)


def as_error2(mssg: str, error: str):
    as_error(mssg)
    print("❌", f'{COL_BLURED}{error}{COL_RESET}\n')


def input_user_str(mssg: str) -> str:
    """ ask a question to user.
    When called in a try..except block, it might prevent issues
    with user possible inputs.
    Parameter(s): mssg is the question asked to user.
    Returns : input user as string. """
    answer = input(f'{COL_QUERY}{mssg}{COL_ORANGE}   ')
    print(f'{COL_RESET}')
    return answer


def input_user_yes(mssg: str, pos_answers=["y", "yes"]) -> bool:
    """ yes or else question to user, supplemented with an ending (Y / N).
    returns : a boolean.
        True if answer is in pos_answers . False for any other case"""
    try:
        answer = input(f'{COL_QUERY}{mssg} (y / n) ? {COL_RESET}')
    except (EOFError):
        as_error("\nError : unexpected end of file !")
        return False
    return answer.lower() in pos_answers


if __name__ == "__main__":
    mess = "Hello World !"
    as_title(mess)
    as_title2(mess)
    as_result(mess)
    as_status(mess)
    as_check(mess)