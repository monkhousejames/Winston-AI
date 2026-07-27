class NotesManager:
    def add_note(self, note):
        with open(self.file_path, "a") as file:
            file.write(note + "\n")

        return f'"{note}" was noted, sir.'

    def __init__(self):
        self.file_path = "data/notes.txt"