import media
import fresh_tomatoes

# listing of all films
toystory = media.Movie("Toy Story", "A story of a boy and his toys", "http://thumbs1.ebaystatic.com/d/l225/m/mBjP-9Mq9FiaQcgEJngDq3g.jpg", "https://www.youtube.com/watch?v=o9nTW1gRJKg")
avatar = media.Movie("Avatar", "A story about aliens", "https://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School of Rock", "Story about music", "http://img.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg", "https://www.youtube.com/watch?v=yMvpJDbWX_c")
midnight_in_paris = media.Movie("Midnight in Paris", "Story about Paris", "https://ia.media-imdb.com/images/M/MV5BMTM4NjY1MDQwMl5BMl5BanBnXkFtZTcwNTI3Njg3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=FAfR8omt-CY")
ratatouille = media.Movie("Ratatouille", "Story about rats", "https://images-na.ssl-images-amazon.com/images/I/81o%2BNjIcgHL._SL1500_.jpg", "https://www.youtube.com/watch?v=3YG4h5GbTqU")
hunger_games = media.Movie("Hunger Games", "Story about dangerous forest", "https://images-na.ssl-images-amazon.com/images/I/91ikvZgoHZL._SL1500_.jpg", "https://www.youtube.com/watch?v=MXU9eB4gc2Y")

movies = [toystory, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
