"""empty message

Revision ID: 879ec797f9ca
Revises: 095dc55d8f28
Create Date: 2023-05-16 13:57:00.923042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '879ec797f9ca'
down_revision = '095dc55d8f28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('storypost',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('indexnumber', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('school', sa.String(), nullable=True),
    sa.Column('department', sa.String(), nullable=True),
    sa.Column('program', sa.String(), nullable=True),
    sa.Column('completed', sa.Integer(), nullable=True),
    sa.Column('admitted', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('telephone', sa.String(), nullable=True),
    sa.Column('hall', sa.String(), nullable=True),
    sa.Column('nationality', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('work', sa.String(), nullable=True),
    sa.Column('guardian', sa.String(), nullable=True),
    sa.Column('kin', sa.String(), nullable=True),
    sa.Column('relationship', sa.String(), nullable=True),
    sa.Column('marital', sa.String(), nullable=True),
    sa.Column('health', sa.String(), nullable=True),
    sa.Column('extra', sa.String(), nullable=True),
    sa.Column('image_file', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('storypost')
    # ### end Alembic commands ###
