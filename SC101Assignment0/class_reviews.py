"""
File: class_reviews.py
Name:CHA_CHU WAN CHI
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    This program can finds the highest score,lowest score and the class avg,
    There's only class SC001 and class SC101,
    different class don't check together
    """
    cla = input('Which class?: ')
    # User inputs a class name
    time001 = 0
    time101 = 0
    max001 = 0
    max101 = 0
    min001 = 10
    min101 = 10
    avg001 = 0
    avg101 = 0
    if cla == '-1':
        print('No class scores were entered')
        # Input -1, end
    else:
        # First score is maximum, minimum and average
        cla = cla.upper()
        data = int(input('Score: '))
        if cla == 'SC001':
            time001 += 1
            # how many score in 001
            max001 = data
            min001 = data
            avg001 = data
        else:
            # or SC101
            time101 += 1
            # how many score in 101
            max101 = data
            min101 = data
            avg101 = data
        while True:
            cla = input('Which class?: ')
            cla = cla.upper()
            if cla == '-1':
                # input -1 to finish
                break
            else:
                data = int(input('Score: '))
                if cla == 'SC001':
                    time001 += 1
                    if data > max001:
                        # data is bigger the old max, change the max
                        max001 = data
                    if data < min001:
                        # data is smaller the old min, change the min
                        min001 = data
                    avg001 += data
                else:
                    time101 += 1
                    if data > max101:
                        max101 = data
                    if data < min101:
                        min101 = data
                    avg101 += data
        print('=============SC001=============')
        if avg001 == 0:
            print('No score for SC001')
        else:
            avg001 = avg001 / time001
            print('Max (001): ' + str(max001))
            print('Min (001): ' + str(min001))
            print('Avg (001): ' + str(avg001))
        print('=============SC101=============')
        if avg101 == 0:
            print('No score for SC101')
        else:
            avg101 = avg101 / time101
            print('Max (101): ' + str(max101))
            print('Min (101): ' + str(min101))
            print('Avg (101): ' + str(avg101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
