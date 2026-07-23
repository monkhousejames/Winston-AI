from datetime import datetime


class CommandHandler:

    def execute(self, command):

        if command == "help":
            return self.help()

        if command == "time":
            return self.time()

        return "I'm afraid I haven't learned that skill yet, sir."


    def time(self):
        current_datetime = datetime.now()
        current_time = current_datetime.strftime("%H:%M")

        return f"The current time is {current_time}, sir."

    def help(self):
        return """
Available Skills

• help
• hello
• time
• date
• exit
"""