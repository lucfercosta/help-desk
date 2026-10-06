from datetime import datetime

class Ticket:

    next_id = 1

    def __init__(self, title, description, priority):
        self.id = Ticket.next_id
        Ticket.next_id += 1

        self.title = title
        self.description = description
        self.priority = priority

        self.status = "OPEN"

        now = datetime.now()
        self.created_at = now
        self.updated_at = now