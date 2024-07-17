"""empty message

Revision ID: 075ecfb83eaf
Revises: 48aeb6114401
Create Date: 2024-07-17 20:35:50.669725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '075ecfb83eaf'
down_revision = '48aeb6114401'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('qr_code', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('qr_code')

    # ### end Alembic commands ###