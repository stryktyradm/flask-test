"""add relationship many to many

Revision ID: e53da7921f8a
Revises: 26ab1ddf0827
Create Date: 2022-10-13 00:54:54.455294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e53da7921f8a'
down_revision = '26ab1ddf0827'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('movies_actors',
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('films_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], ),
    sa.ForeignKeyConstraint(['films_id'], ['films.id'], ),
    sa.PrimaryKeyConstraint('actor_id', 'films_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies_actors')
    op.drop_table('actors')
    # ### end Alembic commands ###
