class Band:

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        return f"{self.name} ({self.musicians})"

    def play(self):
        playing = ''
        for musician in self.musicians:
            playing = playing + musician.play() + '\n'
        return playing