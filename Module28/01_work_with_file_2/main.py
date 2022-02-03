class File:
    def __init__(self, name, mode):
        self.file = open(name, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


with File("Lor.txt", "w") as f:
    f.write("Privet")
