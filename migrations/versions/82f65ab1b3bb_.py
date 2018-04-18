"""empty message

Revision ID: 82f65ab1b3bb
Revises: 22a21363b335
Create Date: 2018-04-15 09:47:28.472233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82f65ab1b3bb'
down_revision = '22a21363b335'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=225), nullable=True),
    sa.Column('artist', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=225), nullable=True),
    sa.Column('username', sa.String(length=225), nullable=True),
    sa.Column('password', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('songs')
    # ### end Alembic commands ###