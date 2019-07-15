import sys
sys.path.insert(0,'/usr/local/lib/python3.5/dist-packages/rpi_rf')
from rpi_rf import RFDevice
from mycroft import MycroftSkill, intent_file_handler

class Rpirf(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    @intent_file_handler('rpirf.intent')
    def handle_rpirf(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267580, 1, 173) #code, protocol, pulse
        rfdevice.cleanup()
        self.speak_dialog('rpirf')


def create_skill():
    return Rpirf()
