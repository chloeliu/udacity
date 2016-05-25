import webbrowser
class Movie():
    """create movie object to store all movie information"""
    valid_ratings=['G','PG','PG-13','R']
    def __init__(self,movie_title, movie_storyine, movie_poster_image_url, movie_trailer_youtube_url):
	self.title =movie_title  
	self.storyline = movie_storyine
	self.poster_image_url = movie_poster_image_url
	self.trailer_youtube_url = movie_trailer_youtube_url
    def show_trailer(self):
	webbrowser.open(self.trailer_youtube_url)
