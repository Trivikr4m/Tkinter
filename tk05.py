import tkinter as tk
from gtts import gTTS
import os
from playsound import playsound

def text_to_audio():
    text = entry.get()

    if text:
        tts = gTTS(text=text,lang='en')
        audio_file = "temp_audio.mp3"
        tts.save(audio_file)
        playsound(audio_file)
        entry.delete(0,'end')
        os.remove(audio_file)

#create the main window
root=tk.Tk()
root.title("Text to Audio Converter")
entry = tk.Entry(root,width=40)
entry.pack(pady=20)
button = tk.Button(root,text="Convert to audio",command=text_to_audio)
button.pack(pady=10)
root.mainloop()