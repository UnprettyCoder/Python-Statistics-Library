import sympy as sy;

# simple integrating method in Sympy Library [CP]
# simple Sigma method using while function [DP]
# Error -> if Fomula Function have many parameters, cannot use simple func(x)

def DP(x, func, startX, endX):
    rtValue = 0;
    while startX <= endX:
        rtValue += func(startX);
        startX += 1;
    return rtValue;

def CP(x, func, startX, endX):
    x = sy.Symbol("x");
    return sy.integrate(func(x), startX, endX);