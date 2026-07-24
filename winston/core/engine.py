from datetime import datetime
from urllib import response
from winston.core.commands import CommandHandler


class Winston:
    def __init__(self):
        """Initialise Winston."""
        self.version = "0.3"
        self.command_handler = CommandHandler()

    def get_greeting(self):
        """Return an appropriate greeting based on the current time."""
        current_hour = datetime.now().hour

        if current_hour < 12:
            return "Good morning"
        elif current_hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"

    def get_command(self):
        """Get a command from the user."""
        return input("> ").strip().lower()


    def run(self):
        """Start Winston."""
        greeting = self.get_greeting()
       

        print("═" * 55)
        print(f"{'WINSTON v' + self.version:^55}")
        print("═" * 55)
        print()
        print(f"{greeting}, sir. Systems are online.")
        print("How may I assist you today?")
        print()
        while True:
            command = self.get_command()

            command = command.lower().strip()
            

            if command == "exit":
                print("\nGoodbye, sir.")
                print("System shutting down...")
                break

            response = self.command_handler.execute(command)

            print()
            print(response)
            print()

        