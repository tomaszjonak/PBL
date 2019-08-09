#! /usr/bin/env python2.7

from __future__ import print_function
import PyBool_public_interface as Bool
import sys
sys.path.append("../../include/")


if __name__ == "__main__":
    expr = Bool.parse_std("input.txt")
    expr = expr["main_expr"]

    expr = Bool.simplify(expr)

    expr = Bool.nne(expr)

    print(Bool.print_expr(expr))
