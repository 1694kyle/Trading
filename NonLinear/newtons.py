""" The Newton-Raphson method """


def newton(f, df, x, tol=0.001, maxiter=100):
    """
    :param f: The function to solve
    :param df: The derivative function of f
    :param x: Initial guess value of x
    :param tol: The precision of the solution
    :param maxiter: Maximum number of iterations
    :return: The x-axis value of the root,
                number of iterations used
    """
    n = 1

    while n <= maxiter:
        x1 = x - f(x)/df(x)
        if abs(x1 - x) < tol:  # Root is very close
            return x1, n
        else:
            x = x1
            n += 1

    return None, n