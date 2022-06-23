from datetime import datetime


class BaseModel(object):
    def __init__(self, created_at=None, updated_at=None, created_by=None, updated_by=None):
        self.updated_by = updated_by
        self.created_by = created_by
        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = created_at
        if updated_at is None:
            self.updated_at = datetime.now()
        else:
            self.updated_at = updated_at
