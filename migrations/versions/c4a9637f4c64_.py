"""empty message

Revision ID: c4a9637f4c64
Revises: 7d67db16da96
Create Date: 2023-07-17 01:11:29.505400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4a9637f4c64'
down_revision = '7d67db16da96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question_type', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('answer_VouF', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('answer_Mult', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('answer_ValNum', sa.Integer(), nullable=True))
        batch_op.drop_column('answer')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('answer', sa.BOOLEAN(), nullable=True))
        batch_op.drop_column('answer_ValNum')
        batch_op.drop_column('answer_Mult')
        batch_op.drop_column('answer_VouF')
        batch_op.drop_column('question_type')

    # ### end Alembic commands ###
