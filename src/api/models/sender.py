from api.models.base_model import BaseModel


class Sender(BaseModel):
    def __init__(self, sender_id, sender_name, sender_description, sender_last_time_triggered,
                 updated_by, created_by, created_at, updated_at):
        super().__init__(updated_at=updated_at, created_at=created_at, updated_by=updated_by, created_by=created_by)
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.sender_description = sender_description
        self.sender_last_time_triggered = sender_last_time_triggered


class SenderZoom(Sender):
    def __init__(self, sender_id, sender_name, sender_description, sender_last_time_triggered,
                 updated_by, created_by, created_at, updated_at, channel, channel_token):
        super().__init__(sender_id, sender_name, sender_description, sender_last_time_triggered,
                         updated_by, created_by, created_at, updated_at)
        self.channel = channel
        self.channel_token = channel_token


class SenderEmail(Sender):
    def __init__(self, sender_id, sender_name, sender_description, sender_last_time_triggered,
                 updated_by, created_by, created_at, updated_at, email_address):
        super().__init__(sender_id, sender_name, sender_description, sender_last_time_triggered,
                         updated_by, created_by, created_at, updated_at)
        self.email_address = email_address


class SenderPhone(Sender):
    def __init__(self, sender_id, sender_name, sender_description, sender_last_time_triggered,
                 updated_by, created_by, created_at, updated_at, phone_number):
        super().__init__(sender_id, sender_name, sender_description, sender_last_time_triggered,
                         updated_by, created_by, created_at, updated_at)
        self.phone_number = phone_number
