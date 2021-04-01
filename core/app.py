

def menu():
    while True:
        print("""
                \nAIRPORT APP
                \r0) Exit
                """)
        choice = input('Choose action')
        if choice == '0':
            return choice
        else:
            print('Try again')


def app():
    app_running = True
    while app_running:
        choice = menu()

        if choice == '0':
            print('Goodbye')
            app_running = False


if __name__ == "__main__":
    app()
