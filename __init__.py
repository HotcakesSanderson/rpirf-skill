import sys
sys.path.insert(0,'/usr/local/lib/python3.5/dist-packages/rpi_rf')
from rpi_rf import RFDevice
from mycroft import MycroftSkill, intent_file_handler

class Rpirf(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    @intent_file_handler('rpirfon.intent')
    def handle_rpirfon(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267571, 1, 172) #globes code, protocol, pulse
        rfdevice.tx_code(267715, 1, 172) #stand code, protocol, pulse
        rfdevice.cleanup()
        self.speak_dialog('')

    @intent_file_handler('rpirfhomeon.intent')
    def handle_rpirfhomeon(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267571, 1, 172) #globes code, protocol, pulse
        rfdevice.tx_code(267715, 1, 172) #stand code, protocol, pulse
        rfdevice.cleanup()
        self.speak_dialog('rpirf')

    @intent_file_handler('rpirfoff.intent')
    def handle_rpirfoff(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267580, 1, 172) #globes code, protocol, pulse
        rfdevice.tx_code(267723, 1, 173) #stand code, protocol, pulse
        rfdevice.cleanup()
        self.speak_dialog('')

def create_skill():
    return Rpirf()
