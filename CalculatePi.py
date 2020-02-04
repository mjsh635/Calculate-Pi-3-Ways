"""The accuracy of Pi when calculated using the Leibniz Formula is dependant
on the amount of iterations. One fact of this formula is how extremly
slow it converges towards Pi.
"""


def leibniz_formula(iterations):
    """Will run for iterations and approximate Pi
    """

    total = 0
    progress_update_diviser = 0
    progress_update_divider = iterations/10
    add_inverse = True

    # Calculation of pi using the Leibniz Formula
    for index in range(iterations):
        is_odd = (index % 2 == 1)
        if is_odd:
            if add_inverse:
                total += 1/index
                add_inverse = False
            else:
                total -= 1/index
                add_inverse = True

        # Update to progress of calculation
        if index % progress_update_divider == 0:
            progress_update_diviser += 1
            print(f"Currently {progress_update_diviser}/10 completed")

    print(f"By doing: {iterations}-iterations,\
the approximation of pi is {total*4}")


def archimedes(n_value):
    import math

    print(n_value*math.sin(180/n_value))


# based on : https://en.wikipedia.org/wiki/Chudnovsky_algorithm but to more digits

def chudnovsky_algorithm(iterations):
    import decimal
    maxK = 70  
    Czero = 426880 * decimal.Decimal(10005).sqrt()
    Mzero = 1
    Xzero = 1
    Lzero = 13591409
    Kzero = 6
    series_total = 13591409 

    for k in range(1, maxK + 1):
        Lzero += 545140134
        Xzero *= (-262537412640768000)
        Mzero = (Kzero**3 - 16*Kzero) * Mzero / k**3
        series_total += decimal.Decimal(Mzero*Lzero) / Xzero
        Kzero += 12

    pi = Czero / series_total
    return pi

print(chudnovsky_algorithm(1))

