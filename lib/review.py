from database_connection import CONN, CURSOR

class Review:
    def __init__(self, year, summary, employee_id, id=None):
        self.id = id
        self.year = year
        self.summary = summary
        self.employee_id = employee_id

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer.")
        if value < 2000:
            raise ValueError("Year must be 2000 or later.")
        self._year = value

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        if not isinstance(value, str):
            raise ValueError("Summary must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Summary cannot be empty.")
        self._summary = value
employee_id = value
@property
def employee_id(self):
    return self._employee_id

@employee_id.setter
def employee_id(self, value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Employee ID must be a positive integer.")
    self._employee_id = value


    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                year INTEGER,
                summary TEXT,
                employee_id INTEGER
            )
        """)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS reviews")
        CONN.commit()

    def save(self):
        if self.id is None:
            CURSOR.execute("""
                INSERT INTO reviews (year, summary, employee_id)
                VALUES (?, ?, ?)
            """, (self.year, self.summary, self.employee_id))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute("""
                UPDATE reviews
                SET year = ?, summary = ?, employee_id = ?
                WHERE id = ?
            """, (self.year, self.summary, self.employee_id, self.id))
        CONN.commit()

    @classmethod
    def create(cls, year, summary, employee_id):
        review = cls(year, summary, employee_id)
        review.save()
        return review

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM reviews WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], year=row[1], summary=row[2], employee_id=row[3])
        return None
