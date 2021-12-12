"""Prod v0.0.1

Revision ID: b0470f90a5aa
Revises: 349df3acafd2
Create Date: 2021-12-11 20:39:07.860515

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b0470f90a5aa'
down_revision = '349df3acafd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card_bins',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('bin', sa.Integer(), nullable=False),
    sa.Column('interval', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bin')
    )
    op.create_table('user',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('fullname', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cards',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('phrase', sa.String(length=150), nullable=False),
    sa.Column('definition', sa.String(length=500), nullable=False),
    sa.Column('owner', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('no_correct', sa.Integer(), nullable=True),
    sa.Column('no_wrong', sa.Integer(), nullable=True),
    sa.Column('card_bin_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('bin_updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.ForeignKeyConstraint(['card_bin_id'], ['card_bins.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cards')
    op.drop_table('user')
    op.drop_table('card_bins')
    # ### end Alembic commands ###