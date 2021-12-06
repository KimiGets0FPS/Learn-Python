import PySimpleGUI as Gui
from register import registry


def home():
    layout = [
        [Gui.Text("Welcome! Start by signing in or sign up!")],
        [Gui.Text("Username:", size=(15, 1)), Gui.InputText()],
        [Gui.Text("Password:", size=(15, 1)), Gui.InputText()],
        [Gui.Button("Log In")],
        [Gui.Button("Forgot Password"), Gui.Button("Create Account")],
        [Gui.Button("Cancel")]
    ]

    window = Gui.Window("Home Page", layout)

    while True:
        event, values = window.Read()
        if event == "Create Account":
            for key in layout:
                window[key]('')
            registry()
        if event == Gui.WIN_CLOSED or event == "Cancel":
            break
        # Gui.Window(title="Hello World", layout=[[]], margins=(300, 280)).read()
    window.close()


if __name__ == '__main__':
    home()
