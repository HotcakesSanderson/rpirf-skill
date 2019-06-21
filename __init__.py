from mycroft import MycroftSkill, intent_file_handler
from rpi_rf import RFDevice

class Rpirf(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rpirf.intent')
    def handle_rpirf(self, message):
        self.tx_code(267580, 1, 173)
        self.speak_dialog('rpirf')


def create_skill():
    return Rpirf()
