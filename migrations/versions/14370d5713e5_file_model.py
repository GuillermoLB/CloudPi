"""file model

Revision ID: 14370d5713e5
Revises: b931f0044e83
Create Date: 2020-09-03 13:18:09.885473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14370d5713e5'
down_revision = 'b931f0044e83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=256), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_file_filename'), 'file', ['filename'], unique=True)
    op.create_index(op.f('ix_file_timestamp'), 'file', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_file_timestamp'), table_name='file')
    op.drop_index(op.f('ix_file_filename'), table_name='file')
    op.drop_table('file')
    # ### end Alembic commands ###
