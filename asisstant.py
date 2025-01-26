import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import smtplib
import calendar
import math
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class PersonalAssistant:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

        # Configure voice settings
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Index 1 for female voice
        self.engine.setProperty('rate', 150)  # Speed of speech

        # API Keys (Replace with your own)
        self.weather_api_key = "YOUR_OPENWEATHER_API_KEY"
        self.news_api_key = "YOUR_NEWS_API_KEY"

        # Email Configuration
        self.email_address = "your_email@gmail.com"
        self.email_password = "your_app_specific_password"

    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Listen to user's voice input"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                print(f"User: {command}")
                return command.lower()
            except sr.UnknownValueError:
                self.speak("Sorry, I didn't catch that. Could you repeat?")
                return ""
            except sr.RequestError:
                self.speak("Sorry, there was an error with the speech recognition service.")
                return ""

    def get_weather(self, city):
        """Get weather information for a city"""
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if data["cod"] != "404":
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                return f"The temperature in {city} is {temp}°C with {desc}"
            else:
                return "City not found"
        except:
            return "Error fetching weather data"

    def get_news(self):
        """Get top news headlines"""
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={self.news_api_key}"
            response = requests.get(url)
            news = response.json()

            articles = news["articles"][:3]  # Get top 3 articles
            headlines = "Here are the top headlines:\n"

            for i, article in enumerate(articles, 1):
                headlines += f"{i}. {article['title']}\n"

            return headlines
        except:
            return "Error fetching news"

    def send_email(self, to_email, subject, body):
        """Send email"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email_address, self.email_password)
            server.send_message(msg)
            server.quit()

            return "Email sent successfully"
        except:
            return "Error sending email"

    def calculate(self, expression):
        """Perform basic calculations"""
        try:
            return str(eval(expression))
        except:
            return "Error in calculation"

    def set_reminder(self, reminder_text, time_str):
        """Set a reminder (basic implementation)"""
        try:
            with open('reminders.txt', 'a') as f:
                f.write(f"{time_str}: {reminder_text}\n")
            return "Reminder set successfully"
        except:
            return "Error setting reminder"

    def process_command(self, command):
        """Process voice commands"""
        if "weather" in command:
            self.speak("Which city would you like to know the weather for?")
            city = self.listen()
            weather_info = self.get_weather(city)
            self.speak(weather_info)

        elif "news" in command:
            news_info = self.get_news()
            self.speak(news_info)

        elif "calculate" in command:
            self.speak("What would you like to calculate?")
            expression = self.listen()
            result = self.calculate(expression)
            self.speak(f"The result is {result}")

        elif "email" in command:
            self.speak("Who would you like to send an email to?")
            to_email = self.listen()
            self.speak("What's the subject?")
            subject = self.listen()
            self.speak("What's the message?")
            body = self.listen()
            result = self.send_email(to_email, subject, body)
            self.speak(result)

        elif "reminder" in command:
            self.speak("What should I remind you about?")
            reminder_text = self.listen()
            self.speak("When should I remind you? (Format: HH:MM)")
            time_str = self.listen()
            result = self.set_reminder(reminder_text, time_str)
            self.speak(result)

        elif "search" in command:
            self.speak("What would you like to search for?")
            search_query = self.listen()
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            self.speak(f"Here are the search results for {search_query}")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            self.speak(f"The current time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            self.speak(f"Today's date is {current_date}")

        elif "exit" in command or "bye" in command:
            self.speak("Goodbye!")
            return False

        return True

    def run(self):
        """Main loop for the assistant"""
        self.speak("Hello! I'm your personal assistant. How can I help you?")

        running = True
        while running:
            command = self.listen()
            if command:
                running = self.process_command(command)


if __name__ == "__main__":
    assistant = PersonalAssistant()
    assistant.run()