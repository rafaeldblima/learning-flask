"""add fields to role model

Revision ID: 198d43284da6
Revises: dcd5da07076a
Create Date: 2020-05-06 15:41:26.538618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '198d43284da6'
down_revision = 'dcd5da07076a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###