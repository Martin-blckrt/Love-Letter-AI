"""
GUI Module with PySimpleGUI
"""

import PySimpleGUI as sg


def createButton(button_text):
    """
    Fonction qui automatise la création de boutton

    :param button_text: sera affiché sur le bouton,
    et sera aussi le nom de l'event associé (Ex: 'Quitter')
    :return: un élément Button utilisable et initialisé
    """
    return sg.Button(button_text, button_color=('white', 'grey'), size=(6, 2),
                     pad=(5, 5), font=('Arial', 20))


def initializeWindow():
    """
    Initialize the game window and all the elements
    """
    sg.theme('DarkAmber')   # Add a touch of color

    # All the stuff inside your window.
    layout = [[sg.Text('Love Letter', font='Arial 42')],
              [sg.Image('src/assets/title_image.png')],
              [createButton('Ok'), createButton('Quitter')]]

    # Create the Window
    window = sg.Window('Love Letter', layout, size=(500, 500),  finalize=True, resizable=True)


    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if sg.WIN_CLOSED or 'Quitter' in event:  # if user closes window or clicks cancel
            break

    window.close()
