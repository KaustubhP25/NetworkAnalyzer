# MAIN
# BY: KAUSTUBH

from src.display import show_menu, display_logo
from src.capture_packets import *
from src.visualize_data import read_csv, visualize_data
from src.anomaly_detection import detect_anomalies


def main_start():
    menu_list = ["START", "OPTIONS", "EXIT"]
    menu_title = "main-menu"
    choice_selected = False

    display_logo("NAT")
    show_menu(menu_title, menu_list)

    while not choice_selected:
        try:
            print("Your Choice:", end=" ")
            choice = int(input())

            choice_selected = True

        except ValueError:
            print("Invalid Choice")
    if choice == 1:
        start()
    elif choice == 2:
        option()


def start():
    print("CAPTURING PACKETS")
    packet_sniffer("data/packets.csv")
    print("Packet capture complete.")

    print("Reading captured data...")
    df = read_csv("data/packets.csv")

    print("Visualizing data...")
    visualize_data(df)

    print("Detecting anomalies...")
    detect_anomalies(df)


def option():
    choice_selected = False
    menu_title = "OPTIONS-MENU"
    menu_option = ["MAIN-MENU", "REQUIREMENTS"]
    show_menu(menu_title, menu_option)
    while not choice_selected:
        try:
            print("Your Choice:", end=" ")
            choice = int(input())

            choice_selected = True

        except ValueError:
            print("Invalid Choice")
    if choice == 1:
        main_start()
    elif choice == 2:
        requirements()


def requirements():
    pass


if __name__ == '__main__':
    main_start()
