from datetime import datetime
from winston.memory.notes import NotesManager


class CommandHandler:

    def __init__(self):
        self.notes_manager = NotesManager()
        self.commands = {
            
            "help": self.help,
            "time": self.time,
            "hello": self.hello,
            "weather": self.weather,
            "date": self.date,
            
        }

    def execute(self, command):
        if command.startswith("note "):
            parts = command.split(" ", 1)
            return self.notes_manager.add_note(parts[1])
        
        if command in self.commands:
            return self.commands[command]()

        return "I'm afraid I haven't learned that skill yet, sir."

        

    def time(self):
        current_datetime = datetime.now()
        current_time = current_datetime.strftime("%H:%M")

        return f"The current time is {current_time}, sir."

    def hello(self):
        return "Hello, sir. How may I assist you today?"

    def weather(self):
        return "I'm sorry, sir. I don't have access to real-time weather information."

    def date(self):
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")

        return f"The current date is {current_date}, sir."

    def help(self):
        return """
Available Skills

• help
• hello
• time
• date
• weather
• exit
"""