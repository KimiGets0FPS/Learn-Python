import PySimpleGUI as Gui


def registry():
    layout = [
        [Gui.Text("Register a new account")],
        [Gui.Text("Username: ", Gui.InputText())],
        [Gui.Text("Password: "), Gui.InputText()],
        [Gui.Button("Done")],
        [Gui.Button("Cancel: ")]
    ]
    window = Gui.Window("Register", layout)

    while True:
        event, values = window.Read()
        if event == Gui.WIN_CLOSED or event == "Cancel":
            break
        if event == "Done":
            break
    window.close()
