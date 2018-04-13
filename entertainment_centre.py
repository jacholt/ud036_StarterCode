import media
import fresh_tomatoes
import urllib

toystory = media.Movie(urllib.quote("Toy Story"))
avatar = media.Movie(urllib.quote("Avatar"))
school_of_rock = media.Movie(urllib.quote("School of Rock"))
midnight_in_paris = media.Movie(urllib.quote("Midnight in Paris"))
ratatouille = media.Movie(urllib.quote("Ratatouille"))
hunger_games = media.Movie(urllib.quote("Hunger Games"))

movies = [toystory, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
