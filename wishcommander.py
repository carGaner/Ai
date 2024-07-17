from speaker import speak
import datetime
def wishme():
  
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<=11:
        speak("Good Morning Sir. please tell me How may i help you.")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir. please tell me How may i help you.")
    elif hour>=16 and hour<23:
        speak("Good evening Sir. please tell me How may i help you.")
if __name__ == "__main__":
    wishme()