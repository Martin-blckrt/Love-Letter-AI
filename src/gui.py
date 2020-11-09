"""
GUI Module with PySimpleGUI
"""

import PySimpleGUI as sg


def createButton(button_image_path):
    """
    Fonction qui automatise la création de boutton

    :param button_image_path: path de l'image utilisée dans le bouton
    :param button_text: sera affiché sur le bouton,
    et sera aussi le nom de l'event associé (Ex: 'Quitter')
    :return: un élément Button utilisable et initialisé
    """
    return sg.Button(button_color=('white', 'grey'), pad=(5, 5), image_filename=button_image_path, image_size=(50, 50))


def initializeWindow():
    """
    Initialize the game window and all the elements
    """
    sg.theme('DarkAmber')  # Add a touch of color

    # All the stuff inside your window.
    background_image = sg.Image('assets/Background.png')
    button_test = sg.Button(image_subsample=7,
                            button_color=('#FFFFFF', '#FFFFFF'),
                            image_filename='assets/buttons/2players.png',
                            image_size=(170, 50))

    layout = [[button_test], [background_image]]

    # Create the Window
    window = sg.Window("", layout, size=(1700, 1000), finalize=True, resizable=False)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if sg.WIN_CLOSED or 'Quitter' in event:  # if user closes window or clicks cancel
            break
        # TODO: check pq ça explose

    window.close()
    return 0


initializeWindow()
