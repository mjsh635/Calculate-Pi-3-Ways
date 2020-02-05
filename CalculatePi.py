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
    """Calculate pi in radians using archimedes
    method
    """
    import math

    print(n_value*math.sin(180/n_value))


def chudnovsky_algorithm(iterations):
    """Calculate pi to 59 decimal places using the
    chudnovsky algorithm based on : https://en.wikipedia.org/wiki/Chudnovsky_algorithm 
    """
    #import decimal and set precision to 60 digits
    import decimal
    decimal.getcontext().prec = 60

    #declare variable used in the equation and setting
    #them to there k=0 series values
    maxK = iterations 
    Czero = 426880 * decimal.Decimal(10005).sqrt()
    Mzero = 1
    Xzero = 1
    Lzero = 13591409
    Kzero = 6
    series_total = decimal.Decimal(13591409) 
    
    #loop for iterations+1 times, calculating the series total
    for k in range(1, maxK + 1):
        Lzero += 545140134
        Xzero *= (-262537412640768000)
        Mzero = (Kzero**3 - 16*Kzero) * Mzero // k**3
        Kzero += 12
        series_total += decimal.Decimal(Mzero*Lzero) / Xzero

    #contstant value C divided by the calculated total above
    pi = Czero / series_total

    #return Pi approximated to 59 decimal places
    print(pi)

def DemoAllMethods():
    """Use this method to quickly demo 3 methods to approximate pi
    """
    import time

    print("here is the leibniz formula used for 10 million iterations\n")
    time.sleep(1)
    leibniz_formula(10000000)
    time.sleep(3)
    print("\nhere is the archimedes method used with an n_value of 10000")
    time.sleep(1)
    archimedes(10000)
    time.sleep(3)
    print("\nHere is the chudnovsky algorithm that will approximate pi to 40 digits after only 70 iterationsn")
    time.sleep(1)
    chudnovsky_algorithm(70)
    time.sleep(3)


DemoAllMethods()