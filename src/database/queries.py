"""
SELECT QUERIES
"""
from sqlalchemy import and_

from src import db, app
from src.database import models

with app.app_context():
    films = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()
    harry_potter_and_ch_s = db.session.query(models.Film).filter(
        models.Film.title == 'Harry Potter and Chamber of Secrets'
    ).first()
    harry_potter_priz_az = db.session.query(models.Film).filter_by(
        title='Harry Potter and the Prizoner of Azkaban'
    ).first()
    and_statement_harry_potter = db.session.query(models.Film).filter(
        models.Film.title != 'Harry Potter and Chamber of Secrets',
        models.Film.rating >= 7.5
    ).all()
    # print(and_statement_harry_potter)
    second_and_statement_harry_potter = db.session.query(models.Film).filter(
        models.Film.title != 'Harry Potter and Chamber of Secrets',
    ).filter(models.Film.rating >= 7.5).all()
    # print(second_and_statement_harry_potter)
    third_and_statement_harry_potter = db.session.query(models.Film).filter(
        and_(
            models.Film.title != 'Harry Potter and Chamber of Secrets',
            models.Film.rating >= 7.5
        )
    ).all()
    # print(third_and_statement_harry_potter)
    deathly_hallows = db.session.query(models.Film).filter(
        models.Film.title.like('%Deathly Hallows%')
    ).all()
    # print(deathly_hallows)
    deathly_hallows_ilike = db.session.query(models.Film).filter(
        models.Film.title.ilike('%Deathly Hallows%')
    ).all()
    # print(deathly_hallows_ilike)
    harry_potter_sorted_by_length = db.session.query(models.Film).filter(
        models.Film.length.in_([146, 161])
    ).all()
    # print(harry_potter_sorted_by_length)
    harry_potter_not_sorted_by_length = db.session.query(models.Film).filter(
        ~models.Film.length.in_([146, 161])
    ).all()
    # print(harry_potter_not_sorted_by_length)
    harry_potter_by_limit = db.session.query(models.Film).filter(
        ~models.Film.length.in_([146, 161])
    )[:3]
    # print(harry_potter_by_limit)
    """
    QUERYING WITH JOINS
    """
    films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
    # print(films_with_actors)
    a = db.session.query(models.Actor).first()
    print(a)
    print(a.films)
