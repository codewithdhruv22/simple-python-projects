import pyscreenshot
from win10toast import  ToastNotifier
noti = ToastNotifier()
import  datetime
img = pyscreenshot.grab()
img_name = datetime.datetime.now().strftime("%d_%b_%Y_%H_%M_%S_%f.png")
img.save(f"C:/Users/asus/OneDrive/Desktop/Youtube work/Python Projects/Screenshot/{img_name}.png")
noti.show_toast(title="Screenshot Taken",msg="Screenshot Taken Successfully",duration=4)
