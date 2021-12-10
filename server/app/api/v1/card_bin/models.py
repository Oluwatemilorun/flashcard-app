from uuid import uuid4
from uuid import uuid4
from datetime import datetime

from marshmallow import fields, Schema, post_load
from sqlalchemy import Column, DateTime, text
from sqlalchemy.dialects.postgresql import UUID

from app.core.db import db
from app.utils.types import JSON
from app.utils.validators import validate_unique_field


class CardBin(db.Model):
    __tablename__ = 'card_bins'

    id = Column(UUID(as_uuid=True), primary_key=True)

    bin = db.Column(db.Integer, unique=True, nullable=False)
    interval = db.Column(db.BigInteger, nullable=False)
    # cards = db.relationship("Card", back_populates="card_bins", uselist=False, lazy=True)

    created_at = Column(DateTime, server_default=text("NOW()"))
    updated_at = Column(DateTime, server_default=text("NOW()"), server_onupdate=text("NOW()"))

    def __init__(self, bin: int, interval: int) -> None:
        self.id = uuid4()
        self.bin = bin
        self.interval = interval
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __repr__(self):
        return "<CardBin %r>" % self.bin


class CardBinSchema(Schema):
    id = fields.Str(dump_only=True)
    bin = fields.Int(required=True)
    interval = fields.Int(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return CardBin(**data)
