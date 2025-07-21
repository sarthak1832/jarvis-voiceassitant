# 🎙️ Python Voice Assistant

A simple voice assistant built with Python. It listens, responds, and runs basic commands like opening websites, playing songs, and answering questions.

## 🔧 Features

- Greets you based on the time of day
- Searches Wikipedia and reads out short summaries
- Opens websites like:
  - YouTube
  - Google
  - Stack Overflow
- Plays specific songs from YouTube (preset links)
- Tells the current time
- Opens Visual Studio Code
- Listens for a “quit” or “exit” command to stop

## 🛠️ Requirements

- Python 3.x  
- Install dependencies:
  ```bash
  pip install pyttsx3 SpeechRecognition wikipedia

  ▶️ How to Use
	1.	Clone this repo or copy the script
	2.	Run the Python file:
  python jarvis.py

  	3.	Say a command when prompted:
	•	Play sea
	•	Open Google
	•	What’s the time?
	•	Search Albert Einstein on Wikipedia
  
🎵 Music Commands (preset)
  Command        Action
Play sea         Opens a specific YouTube song
Play yo          Another preset song
Play nono        Another preset song
Play mark        Another preset song

💡 Notes
	•	Make sure your mic is working.
	•	You can customize the music dictionary with your own YouTube links.
	•	Currently uses system default voice.

✅ To-do (if you want to expand it)
	•	Add more dynamic music search
	•	Integrate with GPT for smarter responses
	•	Add reminders or notes feature

 Built for fun and function. No dependencies on APIs. Runs locally.
