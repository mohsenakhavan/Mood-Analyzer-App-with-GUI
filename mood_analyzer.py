import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import random

# Download necessary data for sentiment analysis
nltk.download('vader_lexicon')

class MoodAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("Mood Analyzer")
        master.geometry("400x300")
        master.configure(bg='#f0f0f0')

        self.label = tk.Label(master, text="How are you feeling?", bg='#f0f0f0', font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=10)

        self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze_mood, bg='#4CAF50', fg='white')
        self.analyze_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", bg='#f0f0f0', font=("Arial", 12), wraplength=350)
        self.result_label.pack(pady=20)

        self.sia = SentimentIntensityAnalyzer()

    def analyze_mood(self):
        text = self.entry.get()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text.")
            return

        sentiment_scores = self.sia.polarity_scores(text)
        compound_score = sentiment_scores['compound']

        if compound_score >= 0.05:
            mood = "positive"
            suggestion = self.get_positive_suggestion()
        elif compound_score <= -0.05:
            mood = "negative"
            suggestion = self.get_negative_suggestion()
        else:
            mood = "neutral"
            suggestion = self.get_neutral_suggestion()

        result = f"Your mood: {mood}\n\nSuggestion: {suggestion}"
        self.result_label.config(text=result)

    def get_positive_suggestion(self):
        suggestions = [
            "Great! Try to share this positive energy with others.",
            "Excellent! Maybe it's time to take on a new challenge.",
            "Fantastic! This is a good time to start a new project."
        ]
        return random.choice(suggestions)

    def get_negative_suggestion(self):
        suggestions = [
            "Some meditation might help you find calm.",
            "Perhaps listening to soothing music could help.",
            "A short walk in nature might improve your mood."
        ]
        return random.choice(suggestions)

    def get_neutral_suggestion(self):
        suggestions = [
            "How about taking some time for yourself and pursuing your interests?",
            "Maybe talking with a friend could help.",
            "Engaging in a creative activity might boost your spirits."
        ]
        return random.choice(suggestions)

root = tk.Tk()
app = MoodAnalyzerApp(root)
root.mainloop()