"""
GUI Module with PySimpleGUI
"""

import PySimpleGUI as sg



def initializeWindow():
    """
    Initialize the game window and all the elements
    """
    sg.theme('DarkAmber')  # Add a touch of color

    # All the stuff inside your window.

    layout = [[sg.Text("Hello from PySimpleGUI")],
              [sg.Button('2 players')]]

    # Create the Window
    window = sg.Window("Love Letter", layout, size=(1500, 800), finalize=True, resizable=False)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if sg.WIN_CLOSED or 'Quitter' in event:  # if user closes window or clicks cancel
            break
        # TODO: check pq ça explose
        if event == '2 players':


    window.close()
    return 0


initializeWindow()
