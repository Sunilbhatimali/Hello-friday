import ollama
import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

print("🤖 FRIDAY is ready!")
print("🎤 Speak something...")

while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("\n🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)

        print("You:", user_input)

        if user_input.lower() in ["exit", "quit", "bye", "stop"]:
            answer = "Goodbye!"
            print("FRIDAY:", answer)
            subprocess.run(["say", "-v", "Tara", answer])
            break

        print("🧠 Thinking...")

        result = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        answer = result["message"]["content"]

        print("FRIDAY:", answer)

        # FRIDAY Tara voice me bolega
        subprocess.run(["say", "-v", "Tara", answer])

    except sr.UnknownValueError:
        print("FRIDAY: I couldn't understand you.")

    except Exception as e:
        print("Error:", e)

