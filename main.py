import qrcode.image.svg
from prettytable import PrettyTable
import wifi_qrcode_generator as wifi_qrcode

import os


def clear_screen():
    # for windows
    if os.name == "nt":
        _ = os.system("cls")
    # for mac and linux
    else:
        _ = os.system("clear")


def ui_menu():
    """Prints a UI to show the user what are the possible options."""
    menu_table = PrettyTable()
    menu_table.field_names = ["'U'RL", "Social media accounts", "'M'essage", "'W'IFI", "'E'xit"]
    menu_table.add_row(["", "'T'witter", "", "", ""])
    menu_table.add_row(["", "'I'nstagram", "", "", ""])
    menu_table.align["Social media accounts"] = "l"
    print(menu_table)


def qr_code_link_url():
    """Returns a url."""
    url_placeholder = "example.com"
    input_url = input(f"Type in a URL. (e.g. {url_placeholder}): ")
    url = "https://" + input_url
    return url


def qr_code_link_twitter():
    """Returns a twitter account."""
    input_account = input("Type in a Twitter account: @")
    account = "https://twitter.com/" + input_account
    return account


def qr_code_link_instagram():
    """Returns a instagram account."""
    input_account = input("Type in a Instagram account: @")
    account = "https://instagram.com/" + input_account
    return account


def qr_code_message():
    """Returns a simple text message."""
    input_message = input("Type in a message you want to share: ")
    return input_message


def qr_code_link_wifi():
    """Returns a qrcode with wifi name and password."""
    input_wifi_name = input("Type in a wifi name (SSID Name): ")
    input_auth_type = input("Type in the authentication type (WPA, WEP, nopass): ")
    input_wifi_pass = input("Type in the wifi password: ")
    qr = wifi_qrcode.wifi_qrcode(input_wifi_name, False, input_auth_type, input_wifi_pass)
    return qr


def make_qr(input_data):
    """Returns the generated qr code."""
    f = qrcode.image.svg.SvgImage
    qr = qrcode.make(data=input_data, image_factory=f)
    return qr


def save_qrcode(get_qrcode_data):
    """Let's the user specify the filename and saving directory. Saves the generated qr code where user want to."""
    name_filename = input("Name your QR Code SVG file: ")
    filename = name_filename + ".svg"
    cwd = os.getcwd()
    print(f"Your current directory: {cwd}")
    choose_directory = input(f"Do you want to save it in the current directory? (y/n): ").lower()
    if choose_directory == "n":
        filepath = input("Where do you wanna save your QR Code file?: ")
    else:
        filepath = cwd
    path = os.path.join(filepath, filename)
    get_qrcode_data.save(path)
    print(f"Congratulations! Your QR Code was saved at\n{filepath}.")


is_running = True

while is_running:
    print("Welcome to QRLinks2 Generator.\n")
    ui_menu()

    user_choice = input("Please choose what you want to save: ").lower()

    if user_choice == "u":
        input_url = qr_code_link_url()
        qr_code_url = make_qr(input_url)
        save_qrcode(qr_code_url)
        clear_screen()
    elif user_choice == "t":
        input_twitter = qr_code_link_twitter()
        qr_code_twitter = make_qr(input_twitter)
        save_qrcode(qr_code_twitter)
        clear_screen()
    elif user_choice == "i":
        input_instagram = qr_code_link_instagram()
        qr_code_instagram = make_qr(input_instagram)
        save_qrcode(qr_code_instagram)
        clear_screen()
    elif user_choice == "m":
        input_msg = qr_code_message()
        qr_code_msg = make_qr(input_msg)
        save_qrcode(qr_code_msg)
        clear_screen()
    elif user_choice == "w":
        input_wifi = qr_code_link_wifi()
        save_qrcode(input_wifi)
        clear_screen()
    elif user_choice == "e":
        is_running = False
        print("Goodbye.")
    else:
        clear_screen()
