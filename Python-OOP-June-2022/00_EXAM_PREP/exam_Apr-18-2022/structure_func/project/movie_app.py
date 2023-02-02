from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []
        self.users_by_username = {}

    def register_user(self, username: str, age: int):
        user = self.__get_user_by_username(username)
        if user:
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_by_username[user.username] = user
        self.users_collection.append(user)

        return f'{user.username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        if user is None:
            raise Exception("This user does not exist!")
        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__get_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        movie.title = kwargs.get('title', movie.title)
        movie.year = kwargs.get('year', movie.year)
        movie.age_restriction = kwargs.get('age_restriction', movie.age_restriction)

        return f"{user.username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie not in user.movies_owned:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{user.username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        if movie in user.movies_owned:
            raise Exception(f"{user.username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{user.username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{user.username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):

        if not self.movies_collection:
            return "No movies found."
        sorted_movies = sorted(self.movies_collection, key=self.__movie_order_by)

        return '\n'.join(m.details() for m in sorted_movies)


    def __str__(self):
        users_string = 'No users.'
        movies_string = 'No movies.'

        if self.users_collection:
            users_string = ', '.join(u.username for u in self.users_collection)
        if self.movies_collection:
            movies_string = ', '.join(m.title for m in self.movies_collection)

        return f"""All users: {users_string}
All movies: {movies_string}"""

    def __get_user_by_username(self, username) -> User:
        return self.users_by_username.get(username, None)

    @staticmethod
    def __movie_order_by(movie: Movie):
        return -movie.year, movie.title
