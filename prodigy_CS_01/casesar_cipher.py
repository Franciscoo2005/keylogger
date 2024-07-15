
# ASCII upper char = 65-90
# ASCII lower char = 97-122
# user should enter the mode encrpyt or decrpyt
# handle argpase errors
# use pyfiglet
import  argparse


def get_text():
    parser = argparse.ArgumentParser(prog="ceaser cipher encryption", description="this program takes a message and a postive or negative shift value for encryption and decryption")
    parser.add_argument("-e", "--encrypt",  type=str,dest="message_encrypt", help="specify a positive value for encryption,eg:3")
    parser.add_argument("-d", "--decrypt",  type=str,dest="message_decrypt", help="specify a negative value for decryption,eg:-3")
    parser.add_argument("-s", "--shift",  type=int,dest="shift", help="specify -s for decryption")
    args = parser.parse_args()
    return args


def ceaser(text, shift_value):
    list = []
    if text.isalpha():
        for element in text:
            if element.isupper():
                first_value = 65 # ascii offset value
                ascii_value = ord(element) # convert letter to its corresponding ASCII
                index_value = ascii_value - first_value
                shifted_value_each_element = (index_value + shift_value) % 26 + first_value # z= (26+3)% 26 +65
                list.append(shifted_value_each_element)

            elif element.islower():
                first_value = 97 # ascii offset value
                ascii_value = ord(element)
                index_value = ascii_value - first_value
                shifted_value_each_element = (index_value + shift_value) % 26 + first_value  # z= (26+3)% 26 +65
                list.append(shifted_value_each_element)

        for element in list:
            print(chr(element), end="")
    else:
        print("specify text (alphabets) only")


def main():
    if cmd_line_input.message_decrypt:
        if cmd_line_input.shift is not None:
            ceaser(cmd_line_input.message_decrypt, cmd_line_input.shift)
            exit()
        print("\nspecify a SHIFT_PARAMETER, use --help to see help message")
    elif cmd_line_input.message_encrypt:
        if cmd_line_input.shift is not None:
            ceaser(cmd_line_input.message_encrypt, cmd_line_input.shift)
            exit()
        print("\nspecify a SHIFT_PARAMETER, use --help to see help message")
    else:
        print("specify an argument, use --help to see help message")


cmd_line_input = get_text()
main()












