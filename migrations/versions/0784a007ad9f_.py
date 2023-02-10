"""empty message

Revision ID: 0784a007ad9f
Revises: 
Create Date: 2023-02-10 14:07:32.990511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0784a007ad9f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Itinerarys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('itinerary', sa.String(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('start', sa.Time(), nullable=False),
    sa.Column('end', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Itinerarys')
    # ### end Alembic commands ###