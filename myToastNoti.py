#Create Toast Notification Using Python

#pip install win10toast
from win10toast import ToastNotifier
notify = ToastNotifier()
notify.show_toast("I am Titile", "Message Here",duration=3,threaded=True)
print("Another Process Some Code Here")

#To Learn More About This Code
#Checkout My Youtube Channel - https://www.youtube.com/channel/UCmOBuijDvNgUMlqpzrwEBcw
