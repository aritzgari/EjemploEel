#Para instalar pip install Eel
import eel
import time

eel.init('web')


@eel.expose
def tiempopy():
    return time.strftime('%c') + (" el tiempo es desde python no desde javascript.")


eel.start('main.html')
