from sqlmodel import SQLModel, create_engine

sql_file_name = "innocars.db"
sql_url = f"sqlite:///{sql_file_name}"

engine = create_engine(sql_url,echo = True)

def create_tables_db():
    SQLModel.metadata.create_all(engine)

create_tables_db()