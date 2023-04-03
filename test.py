import speech_recognition as sr
import pyttsx3
import openai_secret_manager
import requests
import sys
import openai


 
sys.setrecursionlimit(10**6)
try:
 while True:
  # Initialize the recognizer and the text-to-speech engine
  r = sr.Recognizer()
  engine = pyttsx3.init()

  # Set the rate and volume of the text-to-speech engine
  rate = engine.getProperty('rate')
  engine.setProperty('rate', 150)

  volume = engine.getProperty('volume')
  engine.setProperty('volume', 0.5)

  # Define the audio source (microphone or audio file)
  # Uncomment the following line to use the microphone as the audio source
  source = sr.Microphone()

  # Uncomment the following line to use an audio file as the audio source
  # source = sr.AudioFile('path/to/audiofile.wav')
 
  # Use the recognizer to listen to the audio source and transcribe the speech to text
  with sr.Microphone() as audio:
    print("Saying something....!")
    audio_data = r.listen(audio)

  text = r.recognize_google(audio_data)
  print("Transcribed text:", text)


  #'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'

  #api request to Chat GPT
  # Set up the API endpoint and parameters
  #import requests

  key = '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'
  openai.api_key = key # or use the method we defined earlier

  def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.2,
    )
    return response.choices[0].text.strip()

  prompt = text
  response = generate_response(prompt)
  #print(response)
  # Print the response
  print("\nPrinting Json responce...")
  print(response)
  if(prompt == "exit"):
   break;






  # Use the text-to-speech engine to speak the transcribed text
  engine.say(response)
  engine.runAndWait()
except:
  print("an Error occured")

#C:\Users\espoi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts