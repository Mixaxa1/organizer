from enum import Enum


class RecordType(Enum):
    NOTE = 'Notes'
    REMINDER = 'Reminders'
    TASK = 'Tasks'
    POINT = 'Points'