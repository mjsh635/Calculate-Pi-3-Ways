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


leibniz_formula(10000)
