
from vosk import Model,KaldiRecognizer
import pyaudio

from wishcommander import wishme

import datetime
import face 
from speaker import speak
# ask question to google 
from serachinginweb import ask_question_and_get_answer , get_wikipedia_summary
# Example usage:

class checkaskedquestion:
 
    def remove(original_string, word_to_remove):
        return original_string.replace(word_to_remove, '')

    def simplequestions(self):
        modle = Model("C:\\Users\\computer'\\Documents\\projects\\vosk\\vosk\\vosk-model-en-us-0.42-gigaspeech")
        recoginzer = KaldiRecognizer(modle,16000)
        mic = pyaudio.PyAudio()
        strem = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8193)
        strem.start_stream()
        n = 12
        while True:
            data =  strem.read(9096)
            if n==12:
                print("Listening.......")
                n = 13
            if recoginzer.AcceptWaveform(data):
                n=12
                # print("Listening....")
                print("Recoginizing....")
                commande = recoginzer.Result().lower()
                commander = commande[13:]
                commandes = commander[:-2]
                
                
                    
                time = datetime.datetime.now()
                # commandes = command.items()
                if "your name" in commandes:
                    
                    print(f"user said {commandes}")
                    speak("My name is Jarvis")
                elif "wiki" in commandes:
                    print(f"user said: {commandes}")
                    results = commandes
                    result = self.remove(results,"wiki")
                    print("this " + result)
                    topic = result
                    summary = get_wikipedia_summary(topic, sentences=5)
                    if summary:
                        print(summary)
                        speak(summary)
                elif "introduction" in commandes : 
                    selfintroduce = """Iam JARVIS an AI that has the ability to communicate with humans 
                    i can answer any question which is in my database i have a conenction with wiki"""
                    speak(selfintroduce)
                elif 'search' in commandes : 
                    question = commandes
                    answer = ask_question_and_get_answer(question)
                    print("Answer:", answer)
                    speak(answer)

                elif "your age" in commandes:
                
                    print(f"user said {commandes}")
                    speak("I am 19:90 years old")
                elif "name is jarvis" in commandes:
                    print(f"user said {commandes}")
                    speak("Yap you are right.")
                elif "my name" in commandes:
                    
                    face.main(True)
                    print(f"user said{ commandes }")
                    f = open("a.txt","r")
                    name = f.read()
                    speak(f"so your name is {name}")
                    f.close()
                        
                    #  play this game so it should play game which i have made 
                    
                
                    # speak("you are Unknown")
                elif "you are cool" in commandes:
                    print(f"user said {commandes}")
                    speak("Thank you sir For your complement")
                elif "you fine" in commandes:
                    print(f"user said {commandes}")
                    speak("I am completely fine.")
                elif "more information about you" in commandes:
                    print(f"user said {commandes}")
                    speak("""I am an offline ai devloped for simple question i am the only ai that can work both offline and online
                        i can only give more information in online than in offline. my name is derived from the ai jarvis.""")
                elif "help" in commandes:
                
                    print(f"user said {commandes}")
                    speak("I can help you with any problem which is in my data like ask me samall question.")
                elif "the time" in commandes:
            
                    print(f"user said {commandes}")
                    speak(time)
                elif "text mode" in commandes:
                    commandes = input("enter your request: ")
                elif "what can you do" in commandes:
                    print(f"user said {commandes}")
                    speak("""Iam an AI that can communicate with you to do  stuff with in offline """)
                elif "+" in commandes:
                    try:
                        speak(eval(commandes)) 
                        print(f"user said: {commandes}")
                    except Exception as e:
                        print("only number are allowed ")
                    
                # elif "exit" or "quit" in commandes:
                #     try:
                #         speak("you are exited from the base")
                #         print("you are exited from the base")
                #         exit()
                #     except Exception as e:
                #         print("eror 00o0")
                elif "connect" in commandes:
                    print(f"user said : {commandes}")  # iam a java coder 
                    if "internet" in commandes:
                        speak("yes ican connect to internet and i cn use it provide you the data")
                elif "wifi" in commandes or "wi-fi" in commandes:
                    if "turn on" in commandes:
                        speak("yes i can turn on the wifi in your computer")
                    if "turn off" in commandes:
                        speak("yes i can turn it off")
                    print(f"user said {commandes}")
                
                else:
                    # print("recoginzeing...")
                    # time.sleep(1)
                    
                    print(f"user said: {commandes}")
                    # speak("the command is not avilable")
                
                    
        # except Exception as e :
            # print(f"error {e}")
if __name__ == "__main__":
    checkaskedquestion().simplequestions()