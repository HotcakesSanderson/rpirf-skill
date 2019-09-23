import sys
sys.path.insert(0,'/usr/local/lib/python3.5/dist-packages/rpi_rf')
from rpi_rf import RFDevice
from mycroft import MycroftSkill, intent_file_handler

class Rpirf(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
#turn on both lights
    @intent_file_handler('rpirfon.intent')
    def handle_rpirfon(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267571, 1, 172) #globes code, protocol, pulse
        rfdevice.tx_code(267715, 1, 172) #stand code, protocol, pulse
        rfdevice.cleanup()
#turn on the shelf lights
    @intent_file_handler('rpirfonshelf.intent')
    def handle_rpirfonshelf(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267571, 1, 172) #globes code, protocol, pulse
        rfdevice.cleanup()
#turn on the corner light
    @intent_file_handler('rpirfoncorner.intent')
    def handle_rpirfoncorner(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267715, 1, 172) #stand code, protocol, pulse
        rfdevice.cleanup()
#turn on both lights and respond welcome home
    @intent_file_handler('rpirfhomeon.intent')
    def handle_rpirfhomeon(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267571, 1, 172) #globes code, protocol, pulse
        rfdevice.tx_code(267715, 1, 172) #stand code, protocol, pulse
        rfdevice.cleanup()
        self.speak_dialog('rpirf')
#turn off both lights
    @intent_file_handler('rpirfoff.intent')
    def handle_rpirfoff(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267580, 1, 172) #globes code, protocol, pulse
        rfdevice.tx_code(267724, 1, 173) #stand code, protocol, pulse
        rfdevice.cleanup()
#turn off shelf light
    @intent_file_handler('rpirfoffshelf.intent')
    def handle_rpirfoffshelf(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267580, 1, 172) #globes code, protocol, pulse
        rfdevice.cleanup()
#turn off Corner light
    @intent_file_handler('rpirfoffcorner.intent')
    def handle_rpirfoffcorner(self, message):
        rfdevice = RFDevice(17) #default gpio pin
        rfdevice.enable_tx()
        rfdevice.tx_code(267724, 1, 173) #stand code, protocol, pulse
        rfdevice.cleanup()

def create_skill():
    return Rpirf()
