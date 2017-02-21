# -*- coding: utf-8 -*-

import state

def command_calculator(expr):
    """
    Evaluates simple mathematical expression.
    @param expr: math expression
    @type expr: str
    @return: result of the expression
    @rtype: state.done
    """

    # Note that this is _HUGE_ security hole
    # if you tend to use eval in your code, you're
    # probably doing something the wrong way.
    # Numexpr (for instance) could be used here, but 
    # we'll stick to the evil eval for now.
    rval = eval(expr)

    # Or (in case of this rather simple problem)
    # you could sanitize the input, so it contains
    # only allowed data: numbers, +-*/()
    #
    # import re
    # expr = re.sub(r"[^()0-9*/+-]", "", expr)
    # rval = state.done(eval(expr))
    return state.done(rval)

