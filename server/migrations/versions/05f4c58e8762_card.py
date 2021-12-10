"""card

Revision ID: 05f4c58e8762
Revises: 554cd9c286d4
Create Date: 2021-12-10 09:01:43.080406

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '05f4c58e8762'
down_revision = '554cd9c286d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card_bins',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('bin', sa.Integer(), nullable=False),
    sa.Column('interval', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bin')
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
    op.drop_table('card_bins')
    # ### end Alembic commands ###
