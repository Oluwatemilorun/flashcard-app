"""interval

Revision ID: 349df3acafd2
Revises: 05f4c58e8762
Create Date: 2021-12-10 10:48:31.486854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '349df3acafd2'
down_revision = '05f4c58e8762'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('card_bins', 'interval', nullable=False, type_=sa.BigInteger())
    


def downgrade():
    op.alter_column('card_bins', 'interval', nullable=False, type_=sa.Integer())
