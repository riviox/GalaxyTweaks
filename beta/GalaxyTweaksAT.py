import eel

eel.init('web')

@eel.expose
def perform_action(option):
    print(f"Selected option: {option}")

@eel.expose
def get_username():
    import os
    return os.getenv("USERNAME")

eel.start('menu.html', size=(600, 400))
