'''
POLYMORPHISM --> it allows the same method to do different tasks depending on the object.

advantage :
1)flexible
2)Reduce code size
'''

class Messenger:
    def use_keyboard(self):
        print('use keyboard')
    def send_message(self):
        print('sent a message')
    def receive_message(self):
        print('receive a message')

class Whatsapp(Messenger):
    def send_message(self):
        print('sent using WA Text, video, audio')
    def receive_message(self):
        print('receive using WA Text, video, audio')
    def send_live_location(self):
        print('live location sent using WA')

class Facebook(Messenger):
    def send_message(self):
        print('sent using FB Text, video, audio')
    def receive_message(self):
        print('receive using FB Text, video, audio')
    def use_builtin_apps(self):
        print('using builting apps using FB')

class Instagram(Messenger):
    def send_message(self):
        print('sent using IM Text, video, audio')
    def receive_message(self):
        print('receive using IM Text, video, audio')
    def add_filter(self):
        print('filters using Insta')

# WRITE THESE 3 LINES --> 
def use_messenger(ref):
    ref.use_keyboard()
    ref.send_message()
    ref.receive_message()
    if type(ref) == Whatsapp: # duck types 
        ref.send_live_location() 
    if type(ref) == Facebook:
        ref.use_builtin_apps()
    if type(ref) == Instagram:
        ref.add_filter()

w = Whatsapp()
f = Facebook()
i = Instagram()

use_messenger(w)
use_messenger(f)
use_messenger(i)

# INSTEAD OF THESE 9 LINES --> 

# w.use_keyboard()
# w.send_message()
# w.receive_message()

# f.use_keyboard()
# f.send_message()
# f.receive_message()

# i.use_keyboard()
# i.send_message()
# i.receive_message()

