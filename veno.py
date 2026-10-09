import ollama
import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

print("FRIDAY is ready! 🚀")
print("Say 'exit' to quit.")

while True:
    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

        print("🧠 Thinking...")

        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)

        if user_input.lower() in ["exit", "quit", "bye"]:
            response_text = "Goodbye. See you later!"
            print("FRIDAY:", response_text)
            subprocess.run(["say", response_text])
            break

        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        response_text = response["message"]["content"]

        print("FRIDAY:", response_text)

        subprocess.run(["say", response_text])

    except sr.UnknownValueError:
        print("FRIDAY: Sorry, I didn't understand that.")

    except sr.RequestError as e:
        print("Speech recognition error:", e)

    except KeyboardInterrupt:
        print("\nFRIDAY stopped.")
        break
