from datetime import datetime
from api import db
from api.db import BaseModelMixin


class Alert(db.Model, BaseModelMixin):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.String(255), nullable=False)
    updated_by = db.Column(db.String(255), nullable=False)

    def __init__(self, name, description: str = None, created_at=None, updated_at=None, created_by='system', updated_by='system'):
        super().__init__(updated_at=None, created_at=None, updated_by=None, created_by=None)
        self.name = name
        self.description = description
        self.created_by = created_by
        self.updated_by = updated_by
        self.created_at = datetime.now() if created_at is None else created_at
        self.updated_at = datetime.now() if updated_at is None else updated_at

    def __repr__(self):
        return f'Alert({self.name})'

    def __str__(self):
        return f'Alert: {self.name}, created_by {self.created_by} at {self.created_at}'

