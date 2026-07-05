from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
STRICT_DATABASE = os.getenv("JOB_STORE_STRICT_DATABASE", "false").lower() == "true"

def _build_engine(database_url: str):
    """Create the SQLAlchemy engine, using SQLite as a local fallback."""
    connect_args = {}
    if database_url.startswith("sqlite"):
        connect_args["check_same_thread"] = False

    return create_engine(
        database_url,
        echo=False,
        pool_pre_ping=True,
        connect_args=connect_args,
    )


try:
    engine = _build_engine(DATABASE_URL)
except ModuleNotFoundError:
    if STRICT_DATABASE:
        raise
    engine = _build_engine("sqlite:///./app.db")

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db():
    """Yield a database session for request-scoped FastAPI dependencies."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
