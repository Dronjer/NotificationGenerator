import time
from win10toast import ToastNotifier


toaster = ToastNotifier()
def dosthing():
    toaster.show_toast('Notification', 'Drink Water', duration= 2)

delay = 30
while(True):
    dosthing()
    time.sleep(delay)
