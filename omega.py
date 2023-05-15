import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import pyjokes

# Initialize pyttsx3 for text to speech conversion
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)  # Setting male voice, 1 for female voice

# Function to convert text to speech
def speak(audio):
    engine.say(audio)  # Saying the text
    engine.runAndWait()  # Waiting for speech to finish

# Function to listen and recognize speech
def take_command():
    r = sr.Recognizer()  # Initialize recognizer
    with sr.Microphone() as source:  # Use microphone as source
        print("Hey There! I'm Listening...")
        r.pause_threshold = 2  # Time to wait before stopping recording
        audio = r.listen(source)  # Listen to source
    try:
        print("Trying to recognize...")
        query = r.recognize_google(audio, language='en-in')  # Recognize the speech
        print("User has said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that.")
        return "None"
    return query

# Main function
if __name__ == '__main__':
    speak("You have Activated Omega Voice Assistant. What can I do for you?")
    while True:
        query = take_command().lower()  # Take user command and convert to lower case

        # Bunch of conditional statements checking for keywords in user's command
        if 'who are you' in query:
            speak("I am Omega, your personal voice assistant. I'm here to make your life easier!")

        elif 'what can you do' in query:
            speak("I can perform many tasks, like searching the internet, reading the news, "
                  "opening applications, setting an alarm, and much more. You can ask me anything!")

        elif 'who created you' in query:
            speak("I was created by Fahad Ahmad Khan in Python, a very talented programmer.")

        elif 'how do you work' in query:
            speak("I work by converting your voice into text, understanding the intent behind it, "
                  "and then performing the corresponding action. I use various Python libraries "
                  "and APIs to accomplish these tasks.")

        elif 'why are you named' in query:
            speak("I was named after the greek letter Omega")

        elif 'are you a robot' in query:
            speak("Yes, I am a virtual assistant designed to simulate human conversation and perform tasks.")
        
        elif 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            
        elif 'what is the time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The current time is {current_time}")

        elif 'open word' in query:
            speak("opening Microsoft Word")
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')

        elif 'open excel' in query:
            speak("opening Microsoft Excel")
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE')

        elif 'open powerpoint' in query:
            speak("opening Microsoft PowerPoint")
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE')

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shutdown system' in query:
            speak("Shutting down the system")
            os.system('shutdown /s /t 1')
  
        elif 'restart system' in query:
            speak("Restarting the system")
            os.system('shutdown /r /t 1')
  
        elif 'sleep system' in query:
            speak("Sleeping the system")
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        elif 'are you' in query:
            speak("I am Khan developed by Fahad Khan")
        elif 'how are you' in query:
            speak("I'm doing great, thank you!")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'open notepad' in query:
            speak("opening Notepad")
            os.startfile('C:\\Windows\\system32\\notepad.exe')
        elif 'search google' in query:
            from googlesearch import search
            speak("What should I search on Google?")
            search_query = take_command().lower()
            for url in search(search_query, num_results=5):
                speak(url)

        elif 'send email' in query:
            import smtplib
            speak("What should I say?")
            content = take_command().lower()
            to = "fahadahmadk47@gmail.com"  # please replace with your email
            speak("Sending email...")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('your_email@example.com', 'your_password')  # please replace with your email and password
            server.sendmail('your_email@example.com', to, content)
            server.close()
            speak("Email sent!")
        elif 'set an alarm' in query:
            import datetime
            import time
            import winsound
            speak("What time should I set the alarm for? Please specify in HH:MM format.")
            alarm_time = take_command().lower()
            alarm_hour = alarm_time.split(':')[0]
            alarm_minute = alarm_time.split(':')[1]
            while True:
                if (int(datetime.datetime.now().hour) == int(alarm_hour) and
                        int(datetime.datetime.now().minute) == int(alarm_minute)):
                    winsound.Beep(2500, 1000)
                    speak("Time's up!")
                    break

        elif 'tell me a quote' in query:
            import requests
            quote_url = "https://api.quotable.io/random"
            quote_response = requests.get(quote_url).json()
            speak(f"{quote_response['content']} - {quote_response['author']}")

        elif 'calculate' in query:
            speak("What do you want to calculate? Please say the expression.")
            expression = take_command().lower()
            result = eval(expression)
            speak(f"The result is {result}")
        
        elif 'thank' in query:
            speak("Anytime, glad I was helpful. Let me know if you have more questions or tasks")


        elif 'bye' in query or 'stop' in query or 'exit' in query or 'quit' in query:
            speak("Sure thing, Hope I was helpful. Goodbye!")
            exit() #exit program

