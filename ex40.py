class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_Song(self):
        for line in self.lyrics:
            print line
      
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
                    
bulls_on_parade = Song(["They rally around that family",
                        "With pokets full of shells"])
                        
Some_one_like_you = Song(["I beg you'll find someone like me again.",
                         "But you'll lose your mind finally."])

                        
happy_bday.sing_me_a_Song()

bulls_on_parade.sing_me_a_Song()

Some_one_like_you.sing_me_a_Song()