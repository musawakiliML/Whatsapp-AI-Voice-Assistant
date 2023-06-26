from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config


#Database connection url
url = URL.create(
    drivername='postgresql',
    username=config('DB_USER'),
    password=config('DB_PASSWORD'),
    host='localhost',
    database='my_ai_bot_assistant',
    port=5432
)

# Establishing Database Connection
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Conversations(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    message = Column(String)
    response = Column(String)


Base.metadata.create_all(engine)