"""

"""
# ------------------------------------------------------- #
#                     imports
# ------------------------------------------------------- #
import tkinter

import os

from logic.rand_func import get_numbers

# ------------------------------------------------------- #
#                   definitions
# ------------------------------------------------------- #


# ------------------------------------------------------- #
#                   global variables
# ------------------------------------------------------- #


# ------------------------------------------------------- #
#                      functions
# ------------------------------------------------------- #
def main_window_function():
    main_window = tkinter.Tk()
    main_window.title("Verlosungs Tool")
    main_window.iconbitmap("..//graphics//app_icon.ico")
    main_window.geometry("250x150")
    main_window.maxsize(250, 150)

    number_of_winners_var = tkinter.IntVar()
    number_of_winners_label = tkinter.Label(main_window, text="Enter number of contestants:")
    number_of_winners_label.pack(fill='x', expand=True)
    number_of_winners_entry = tkinter.Entry(main_window, textvariable=number_of_winners_var)
    number_of_winners_entry.pack(fill='x', expand=True)
    number_of_winners_entry.focus()

    number_of_devices_var = tkinter.IntVar()
    number_of_devices_label = tkinter.Label(main_window, text="Enter number of Devices:")
    number_of_devices_label.pack(fill='x', expand=True)
    number_of_devices_entry = tkinter.Entry(main_window, textvariable=number_of_devices_var)
    number_of_devices_entry.pack(fill='x', expand=True)
    number_of_devices_entry.focus()

    run_button = tkinter.Button(main_window, text="Get Winners", width=25, command=lambda: list_window(number_of_winners_var.get(), number_of_devices_var.get()))
    exit_button = tkinter.Button(main_window, text="Stop App", width=25, command=main_window.destroy)
    run_button.pack()
    exit_button.pack()

    main_window.protocol("WM_DELETE_WINDOW", disable_event)
    main_window.mainloop()


def list_window(number_of_winners, number_of_devices):
    result = get_numbers(number_of_winners, number_of_devices)

    with open("result.txt", "w") as file:
        for winner in result:
            file.write(str(winner))
            file.write("\n")
    file_to_open = open("result.txt", "r")
    print(file_to_open.read())
    open_result()


def disable_event():
    pass


def open_result():
    command_run = "notepad.exe result.txt"
    os.system(command_run)

# ------------------------------------------------------- #
#                      classes
# ------------------------------------------------------- #


# ------------------------------------------------------- #
#                       main
# ------------------------------------------------------- #
