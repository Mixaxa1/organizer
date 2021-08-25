import sqlite3

from Record_type import RecordType


class DataBaseWork:
    def __init__(self):
        self.con = sqlite3.connect("Records.db")
        self.cur = self.con.cursor()

    def get_record_info(self, record_type, id):
        return self.cur.execute("""SELECT * FROM """ + record_type + """ WHERE id = ?""", (id,)).fetchone()

    def save_new_record(self, record_type, title, topic, description, add_date_time, signal_date_time):
        cells = 'title, topic, description, add_date_time'
        values_str = "?, ?, ?, ?"
        values = [title, topic, description, add_date_time, signal_date_time]
        values = [elem for elem in values if elem != '']

        if record_type == RecordType.REMINDER.value:
            cells += ', signal_date_time'
            values_str += f', ?'
        elif record_type == RecordType.TASK.value:
            cells += ', signal_date_time, completed'
            values_str += ', ?, ?'
            values.append(False)

        operation = f"INSERT INTO {record_type}({cells}) VALUES({values_str})"

        self.cur.execute(operation, values)
        self.con.commit()

    def save_edited_record(self, record_type, id, title, topic, description, signal_date_time):
        operation_part = f'title = ?, topic = ?,description = ?'
        values = [title, topic, description, id]

        if record_type in [RecordType.REMINDER.value, RecordType.TASK.value]:
            operation_part += f', signal_date_time = ?'
            values.insert(3, signal_date_time)

        operation = f'UPDATE {record_type} SET {operation_part} WHERE id = ?'

        self.cur.execute(operation, values)
        self.con.commit()

    def save_points(self, id, points_le):
        for point in points_le:
            self.cur.execute("""INSERT INTO Points(task_id, title, toggled) VALUES(?, ?, ?)""",
                            (id, point[0].text(), False))
        self.con.commit()

    def save_edited_points(self, id, points_le):
        for point in points_le:
            if point[1]:
                self.cur.execute("""UPDATE Points SET title = ? WHERE ID = ?""", (point[0].text(), point[1]))
            else:
                self.cur.execute("""INSERT INTO Points(task_id, title, toggled) VALUES(?, ?, ?)""",
                                 (id, point[0].text(), False))
            self.con.commit()

    def delete_record(self, id, record_type):
        self.cur.execute("""DELETE FROM """ + record_type + """ WHERE id = ?""", (id,))
        self.con.commit()

    def get_records_by_type(self, record_type):
        return self.cur.execute("""SELECT * FROM """ + record_type).fetchall()

    def get_record(self, record_type, id):
        return self.cur.execute("""SELECT * FROM """ + record_type + """ WHERE id = ?""", (id,)).fetchone()

    def get_id(self, type_record, title):
        return self.cur.execute("""SELECT id FROM """ + type_record + """ WHERE title = ?""", (title,)).fetchone()[0]

    def check_record(self, record_type, title):
        return self.cur.execute("""SELECT * FROM """ + record_type + """ WHERE title = ?""", (title,)).fetchone()

    def get_points(self, id):
        return self.cur.execute("""SELECT * FROM Points WHERE task_id = ?""", (id,)).fetchall()

    def update_point_state(self, state, id):
        self.cur.execute("""UPDATE Points SET toggled = ? WHERE id = ?""", (state, id))
        self.con.commit()

    def complete_task(self, id):
        self.cur.execute("""UPDATE Tasks SET completed = ? WHERE id = ?""", (True, id))
        self.con.commit()