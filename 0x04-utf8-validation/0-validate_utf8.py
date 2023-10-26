#!/usr/bin/python3
'''UTF-8 Validation'''


def validUTF8(data):
    '''a function that determines if a given
    data set represents a valid UTF-8 encoding.'''

    word_count = 0
    idx = False
    new_dict = {}
    for i, num in enumerate(data):
        if (num >= 256):
            #print("Error, too large")
            return False
        bin_num = bin(num).replace("0b", "")
        if len(bin_num) < 8:
            x = 8-len(bin_num)
            bin_num = ("0"*x) + bin_num

        if check_bin(bin_num):
            new_dict[word_count] = [bin_num]
            word_count += 1
        elif check_f(bin_num):
            if word_count == 0:
                #print(new_dict, "\nerror found 1")
                return False
            new_dict[word_count-1].append(bin_num)
        else:
            #print(new_dict, "\nerror found 2")
            return False
    
    # TODO - write code to check each character, covert them to numbers, and confirm the limit
    for i in new_dict.values():
        bin_num = "".join(i)
        dec = int(bin_num, 2)

        if bin_num.startswith('0'):
            if dec >= 0 and dec <= 127:
                #print(1)
                return True
        elif bin_num.startswith('110'):
            if dec >= 49792 and dec <= 57279:
                #print(2)
                return True
        elif bin_num.startswith('1110'):
            if dec >= 14721152 and dec <= 15712191:
                #print(3)
                return True
        elif bin_num.startswith('11110'):
            if dec >= 4036001920 and dec <= 4103061439:
                #print(4)
                return True

    #print_dict(new_dict)

    return False


def check_bin(num):
    '''check if it is a new word and
    return the number of byte, else False'''

    if num.startswith('0'):
        return 1
    elif num.startswith('110'):
        return 2
    elif num.startswith('1110'):
        return 3
    elif num.startswith('11110'):
        return 4

    return False


def check_f(num):
    '''check if a num is a follow up of a character'''

    if num.startswith('10'):
        return True
    
    return False

def print_dict(dicti):
    for i, j in dicti.items():
        print(i, ':', j)



#data = [65]
#print(validUTF8(data))

#data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
#print(validUTF8(data))

#data = [229, 65, 127, 2563]
#print(validUTF8(data))
#print(validUTF8([65, 80, 256, 32, 182, 181, 183, 32, 121, 116, 237, 163, 184, 182, 163, 80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33, 229, 65, 127]))