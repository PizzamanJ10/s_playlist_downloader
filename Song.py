
#This is the song class. A song object has a name attribute, artist, and wether it has a youtube link.
class Song:
    
  #Class constructor
  def __init__(self, name, artist):
    self.name = name
    self.artist = artist
    self.has_youtube = False


  #ToString function
  def __str__(self):

    artist_string = ""

    #add artists to artist string
    for artist in self.artist:
      artist_string = artist_string + artist + ", "

    artist_string = artist_string[:len(artist_string)-2]

    return self.name + ", by " + artist_string