"""empty message

Revision ID: 4881be060a46
Revises: 
Create Date: 2020-07-16 18:23:18.537635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4881be060a46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temp_reading',
    sa.Column('date_time', sa.Float(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('humidity', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('date_time')
    )
    op.create_index(op.f('ix_temp_reading_humidity'), 'temp_reading', ['humidity'], unique=False)
    op.create_index(op.f('ix_temp_reading_temperature'), 'temp_reading', ['temperature'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_temp_reading_temperature'), table_name='temp_reading')
    op.drop_index(op.f('ix_temp_reading_humidity'), table_name='temp_reading')
    op.drop_table('temp_reading')
    # ### end Alembic commands ###
