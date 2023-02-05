from project.movie_specification.movie import Movie


class Thriller(Movie):
    MIN_AGE_RESTRICTION = 16
    AGE_RESTRICTION_ERROR_MESSAGE = "Thriller movies must be restricted for audience under 16 years!"

    def __init__(self, title, year, owner, age_restriction=None):
        age_restriction = age_restriction if age_restriction else self.MIN_AGE_RESTRICTION
        super().__init__(title, year, owner, age_restriction)

    @property
    def type(self):
        return 'Thriller'