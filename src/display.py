# DISPLAY
# BY: KAUSTUBH

from colorama import init, Fore
import pyfiglet

init()


def show_menu(heading, menu_options):
    print(heading.upper())
    for index, option in enumerate(menu_options, start=1):
        print(f"[{index}] - {option}")


def display_logo(letter, color=Fore.GREEN, font="standard"):
    ascii_art = pyfiglet.figlet_format(letter, font=font)
    print(f"{color}{ascii_art}{Fore.RESET}")


def show_error(error_message, error_code):
    print(f"Error{error_code}: {error_message}")
