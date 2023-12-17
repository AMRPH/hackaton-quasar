import eel
from model.model import Quasar
from model.API_KEY import API_KEY

eel.init("")

@eel.expose
def submit_ans(text):
    model = Quasar(API_KEY)
    return model.answer(text)

eel.start("./ui/main.html", size = (900,600))
