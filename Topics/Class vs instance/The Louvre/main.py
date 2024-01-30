class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


n = Painting(input(), input(), int(input()))

print(f"\"{n.title}\" by {n.artist} ({n.year}) hangs in the Louvre.")