import media
import fresh_tomatoes
toy_Story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg", "https://www.youtube.com/watch?v=NBepTulmSMw")
toy_Story.show_trailer()

#print (toy_Story.storyline)

avatator = media.Movie("Avatator Story", "A story of a boy and his toys that come to life", "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg", "https://www.youtube.com/watch?v=NBepTulmSMw")
avatator.show_trailer()

football = media.Movie("Football story", "A story of a boy and his toys that come to life", "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg", "https://www.youtube.com/watch?v=NBepTulmSMw")
football.show_trailer()

#print (toy_Story.storyline)

car = media.Movie("Car story", "A story of a boy and his toys that come to life", "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg", "https://www.youtube.com/watch?v=NBepTulmSMw")
car.show_trailer()

movies = [toy_Story,avatator,football,car]
fresh_tomatoes.open_movies_page(movies)
