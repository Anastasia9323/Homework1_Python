from sqlalchemy import create_engine, inspect
from sqlalchemy import create_engine, text

class CompanyTable:
    
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_companies(self):
        return self.db.execute("SELECT * FROM company").fetchall()


    def get_active_companies(self):
        return self.db.execute("SELECT * FROM company WHERE \"is_active\" = true").fetchall()
