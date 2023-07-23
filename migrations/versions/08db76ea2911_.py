"""empty message

Revision ID: 08db76ea2911
Revises: 4e2e4de7ad27
Create Date: 2023-07-22 17:37:36.687592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08db76ea2911'
down_revision = '4e2e4de7ad27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('answer_Mult_A', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('answer_Mult_B', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('answer_Mult_C', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('answer_Mult_D', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.drop_column('answer_Mult_D')
        batch_op.drop_column('answer_Mult_C')
        batch_op.drop_column('answer_Mult_B')
        batch_op.drop_column('answer_Mult_A')

    # ### end Alembic commands ###
