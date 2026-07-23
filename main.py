from winston.core.engine import Winston


def main():
    """Entry point for the Winston application."""
    assistant = Winston()
    assistant.run()


if __name__ == "__main__":
    main()