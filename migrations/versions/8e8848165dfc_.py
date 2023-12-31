"""empty message

Revision ID: 8e8848165dfc
Revises: c67b2290381e
Create Date: 2023-07-09 14:59:55.778091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e8848165dfc'
down_revision = 'c67b2290381e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    # ### end Alembic commands ###
