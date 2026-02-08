from sqlmodel import create_engine, Session
import config

# Create the database engine
engine = create_engine(config.DATABASE_URL, echo=False)

def get_session():
    with Session(engine) as session:
        yield session