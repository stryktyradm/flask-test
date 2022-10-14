from src.database.models import Film


class FilmService:

    @staticmethod
    def fetch_all_film(session):
        return session.query(Film)

    @classmethod
    def fetch_film_by_uuid(cls, session, uuid):
        return cls.fetch_all_film(session).filter_by(
            uuid=uuid
        ).first()
