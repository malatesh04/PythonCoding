'''
3 types --> 
1)inherited method --> code reusability
2)overridden method --> Method customization
3)specialized method --> add new features
'''

class Messenger:
    def send_message(self):
        print('Text message is sent')
    def receive_message(self):
        print('Text message is received')
class InternalMessenger(Messenger):  # inherited method
    pass
class WhatsappMessenger(Messenger):
    def send_message(self):          # overridden --> method customization method
        print('Text,Photos,Videos and Files sent')
    def receive_message(self):       # overridden --> method customization method
        print('Text,Photos,Videos and Files received')
    def set_dp(self):                # specialized --> new features added
        print('dp is set')
    def set_status(self):            # specialized --> new features added
        print('status is set')

im = InternalMessenger() # creating InternalMessenger object
im.send_message()
im.receive_message()

wm = WhatsappMessenger() # creating WhatsappMessenger object
wm.send_message()
wm.receive_message()
wm.set_dp()
wm.set_status()