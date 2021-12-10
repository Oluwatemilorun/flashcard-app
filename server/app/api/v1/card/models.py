from uuid import uuid4
from datetime import datetime
from marshmallow import fields, Schema, post_load
from sqlalchemy import Column, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID

from app.core.db import db
from app.api.v1.card_bin.models import CardBinSchema


class Card(db.Model):
    __tablename__ = "cards"

    id = Column(UUID(as_uuid=True), primary_key=True)

    phrase = db.Column(db.String(150), nullable=False)
    definition = db.Column(db.String(500), nullable=False)
    owner = Column(UUID(as_uuid=True))
    no_correct = db.Column(db.Integer)
    no_wrong = db.Column(db.Integer)
    current_bin = db.relationship("CardBin", lazy=True)
    card_bin_id = Column(ForeignKey("card_bins.id"), nullable=False)
    bin_updated_at = Column(DateTime, server_default=text("NOW()"))

    created_at = Column(DateTime, server_default=text("NOW()"))
    updated_at = Column(DateTime, server_default=text("NOW()"), server_onupdate=text("NOW()"))

    def __init__(self, phrase: str, definition: str):
        self.id = uuid4()
        self.phrase = phrase.lower()
        self.definition = definition.lower()

        self.no_correct = 0
        self.no_wrong = 0
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        self.bin_updated_at = self.created_at

    def __repr__(self):
        return "<Card %r>" % self.id

class CardSchema(Schema):
    id = fields.Str(dump_only=True)
    phrase = fields.Str(required=True)
    definition = fields.Str(required=True)
    owner = fields.Str(dump_only=True)
    no_correct = fields.Int(dump_only=True)
    no_wrong = fields.Int(dump_only=True)
    bin_updated_at = fields.Str(dump_only=True)
    current_bin = fields.Nested(CardBinSchema, dump_only=True)
    created_at = fields.Str(dump_only=True)
    updated_at = fields.Str(dump_only=True)

    @post_load
    def make_user(self, data, **kwargs):
        return Card(**data)
