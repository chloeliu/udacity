import media
import fresh_tomatoes

# intialize the Movie instance with required fields
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toy come to live",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

avatar = media.Movie(
    "Avatar",
    "A marine on a alient planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=_i2RCBa3l-g"
)

finding_dory = media.Movie(
    "Finding Dory",
    "A fish named Dory trying to find her home",
    "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
    "https://www.youtube.com/watch?v=TAXZRz_j5AQ"
)

sing = media.Movie(
    "Sing",
    "A singing competition amongst animals living in the city",
    "http://cdn.collider.com/wp-content/uploads/2015/11/sing-teaser-poster.jpg",
    "https://www.youtube.com/watch?v=esSjfWbDUck")

zootopia = media.Movie(
    "Zootopia",
    "A rabit turned into a great cop in the city of Zootopia",
    "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
    "https://www.youtube.com/watch?v=bY73vFGhSVk")

angry_bird = media.Movie(
    "Angry Bird",
    "Red bird get super angry at pigs who stole birds' eggs",
    "https://upload.wikimedia.org/wikipedia/en/6/65/Angry_Birds_2016_film_poster.jpg",
    "https://www.youtube.com/watch?v=QRmKa7vvct4")

#put all movie instance into an list to prepare for web page creation
movies = [toy_story, avatar, finding_dory, sing, zootopia, angry_bird]
#generate the web page and open the webpage in default browser
fresh_tomatoes.open_movies_page(movies)
