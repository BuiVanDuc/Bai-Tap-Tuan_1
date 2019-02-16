from datetime import datetime


# exercise 1
def sort_digits_in_number(number):
    # Check number is INT and have 3 digits
    is_integer = isinstance(number, int)
    if is_integer:
        if 100 <= number < 1000:
            new_number = "".join(sorted(str(number), reverse=True))
            print "Output number: {}".format(new_number)
            return new_number
    print "Number is not correct, please input number is INT and have 3 digits"


# Find number of upper and lower alphabet
def find_number_of_upper_and_lower_alphabet(str_startings):
    if str_startings:
        lower_count = sum(1 for c in str_startings if c.islower())
        upper_count = sum(1 for c in str_startings if c.isupper())
        print "Number of upper and lower alphabet are: {} and {}".format(upper_count, lower_count)
        return {"upper_count": upper_count, "lower_count": lower_count}
    print "character is not found, please enter character. Ex:Abcs@123"


def charge_taxi_fare(distance_length):
    MONEY_AT_30000 = 227500
    if distance_length > 0:
        if distance_length <= 1000:
            money = 10000
            print "Total Amount: {:,}VND".format(money)
            return money
        elif distance_length <= 30000:
            money = 10000 + float((distance_length - 1000) * 1500 / 200)
            print "Total Amount: {:,}VND".format(money)
            return money
        elif distance_length > 30000:
            money = MONEY_AT_30000 + (distance_length - 30000) * 8
            print "Total Amount: {:,}VND".format(money)
            return money
    else:
        print "Total Amount: {}VND".format(0)
        return 0


def print_isosceles_triangle(height):
    try:
        if int(height) >= 1:
            number_point = 1
            number_tab = height - 1
            str_start = ""
            for y in range(height):
                for n in range(number_tab):
                    str_start += "\t"
                for x in range(number_point):
                    str_start += "*\t"
                print str_start
                number_tab -= 1
                number_point += 2
                str_start = ""
    except ValueError:
        print "Input is a number integer bigger than zero. Please enter again!"


def is_leap_year(date):
    # check validated form
    try:
        format_date = "%d-%m-%Y"
        date_obj = datetime.strptime(date, format_date)
        if date_obj:
            # Check is leap year
            year_str = date_obj.strftime("%Y")
            # Year have end tow number is 00
            if year_str[-2:] == "00":
                first_two_number = int(year_str[:-2])
                if first_two_number % 4 == 0:
                    print "is leap year"
                    return True
            else:
                end_two_number = int(year_str[-2:])
                if end_two_number % 4 == 0:
                    print "is leap year"
                    return True
            print "not is leap year"
            return False
    except ValueError:
        print "Input date is not correct, please try again. Ex: 30-02-2019"


def standardize_string(text):
    # Check input end standardize top and end string
    if text:
        new_str_1= standardize_top_and_end_string(text)
        if new_str_1:
            new_str_2 = standardize_tab_in_str(new_str_1)
            if new_str_2:
                new_str_3 = standardize_comma_and_point_in_str(new_str_2)
                if new_str_3:
                    return new_str_3


def find_ucln_bcnn(number_1, number_2):

    if number_1 > number_2:
        if number_1 % number_2 == 0:
            ucLn = number_2
            bcnn = number_1
            print "UCLN: {}".format(ucLn)
            print "BCNN: {}".format(bcnn)
            return number_1, number_2
        else:
            ucLn = 1
            for n in range(number_2-1, 0, -1):
                if number_1 % n == 0 and number_2 % n == 0:
                    ucLn = n
                    break
            if ucLn == 1:
                bcnn = number_1 * number_2
                print "BCNN: {}".format(bcnn)
                print "UCLN: {}".format(ucLn)
                return ucLn, bcnn
            else:
                # Find ucnn
                ucnn = 1
                for n in range(1, number_2):
                    if number_1 % n == 0 and number_2 % n == 0:
                        ucnn = n
                        break
                if ucnn != 1:
                    bcnn = number_1 * ucnn
                    print "BCNN: {}".format(bcnn)
                    print "UCLN: {}".format(ucLn)
                    return ucLn, bcnn
    elif number_1 < number_2:
        if number_2 % number_1 == 0:
            ucLn = number_1
            bcnn = number_2
            print "UCLN: {}".format(ucLn)
            print "BCNN: {}".format(bcnn)
            return number_2, number_1
        else:
            ucLn = 1
            for n in range(number_1-1, 0, -1):
                if number_1 % n == 0 and number_2 % n == 0:
                    ucLn = n
                    break
            if ucLn == 1:
                bcnn = number_1 * number_2
                print "BCNN: {}".format(bcnn)
                print "UCLN: {}".format(ucLn)
                return ucLn, bcnn
            else:
                # Find ucnn
                ucnn = 1
                for n in range(1, number_1):
                    if number_1 % n == 0 and number_2 % n == 0:
                        ucnn = n
                        break
                if ucnn != 1:
                    bcnn = number_2 * ucnn
                    print "BCNN: {}".format(bcnn)
                    print "UCLN: {}".format(ucLn)
                    return ucLn, bcnn
    else:
        bcnn = number_2
        ucLn = bcnn
        print "UCLN: {}".format(ucLn)
        print "BCNN: {}".format(bcnn)
        return bcnn, ucLn


def revert_string(text):
    if text:
        new_text = text[::-1]
        return new_text


def standardize_top_and_end_string(text):
    i = 0
    flag = 0
    last_index = 0
    start_index = 0

    while i <= len(text) - 1:
        if flag == 0:
            if text[i] != ' ' and text[i] != ',' and text[i] != '.':
                start_index = i
                flag += 1
        else:
            if text[i] != ' ' and text[i] != ',' and text[i] != '.':
                last_index = i
        i += 1
    if last_index == 0 and start_index == 0:
        print " Chuoi khong co ky tu"
        return text
    elif start_index != 0 and last_index == 0:
        print text[start_index]
        return text[start_index]
    else:
        if last_index <= len(text) - 2:
            if text[last_index + 1] == "," or text[last_index + 1] == ".":
                last_index = last_index + 1

    new_str_1 = text[start_index:last_index + 1]

    return new_str_1


# Input is text is  standardize top and end string
def standardize_tab_in_str(text):
    number_tab = 0
    new_str = ""
    count = 0

    for elemt in text:
        temp_str = elemt
        if temp_str == " ":
            number_tab += 1
            if number_tab > 1:
                temp_str = ''
                number_tab = 1
        else:
            count += 1
            if count > 1:
                number_tab = 0
        new_str += temp_str

    return new_str


# Input is text is  standardize tab in str
def standardize_comma_and_point_in_str(text):
    i = 0
    new_str = ""

    while i < len(text):
        flag_1 = 0
        tem_str = text[i]
        if text[i] == ',' or text[i] == '.':
            for j in range(i + 1, len(text) - 1):
                # find to index is alphabet
                if text[j] != '.' and text[j] != ',' and text[j] != ' ':
                    tem_str = text[i] + " "
                    i = j
                    flag_1 = 1
                    break
        elif text[i] == ' ':
            flag_2 = 0
            for j in range(i + 1, len(text) - 1):
                if text[j] == '.' or text[j] == ',':
                    if flag_2 == 0:
                        tem_str = text[j] + ' '
                        flag_2 = 1
                # find to index is alphabet
                elif text[j] != '.' and text[j] != ',' and text[j] != ' ':
                    if flag_2 == 0:
                        tem_str = text[i]
                    i = j
                    flag_1 = 1
                    break

        new_str += tem_str
        if flag_1 == 0:
            i += 1
    return new_str
