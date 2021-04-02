
menu_choices = {
        0: "Exit",
        1: "Exit",
        2: "Exit",
        }

messages = {
        "welcome": "Hello, welcome to Airport App!"
        }

def menu():
    print(messages.get('welcome'))

    while True:
        print('\n'.join(menu_choices.values()))
        choice = input('Choose action:  ')
        if choice == '0':
            return choice
        else:
            print('Try again.')


def app():
    app_running = True
    while app_running:
        choice = menu()

        if choice == '0':
            print('Goodbye')
            app_running = False


if __name__ == "__main__":
    app()
