
# ASCII upper char = 65-90
# ASCII lower char = 97-122
# user should enter the mode encrpyt or decrpyt
# handle argpase errors
import  argparse


def get_text():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encrypt", dest="text")
    parser.add_argument("-d", "--decrypt", dest="text")
    option = parser.parse_args()
    return option.text


def ceaser(text, shift_value):
    if text.isalpha(): # check if input is text
        for element in text:
            if element.isupper():
                first_value = 65 # ascii offset value
                ascii_value = ord(element) # convert letter to its corresponding ASCII
                index_value = ascii_value - first_value
                shifted_value_each_element = (index_value + shift_value) % 26 + first_value # z= (26+3)% 26 +65
                list_upper.append(shifted_value_each_element)

            elif element.islower():
                first_value = 97 # ascii offset value
                ascii_value = ord(element)
                index_value = ascii_value - first_value
                shifted_value_each_element = (index_value + shift_value) % 26 + first_value  # z= (26+3)% 26 +65
                list_upper.append(shifted_value_each_element)
    else:
        print("input text only")


cmd_line_input = get_text()
list_upper=[]


def result():
    for element in list_upper:
        print(chr(element), end="")


ceaser(cmd_line_input, 3)
result()








