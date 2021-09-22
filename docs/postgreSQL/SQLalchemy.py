from sqlalchemy import create_engine

from config import *

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}/{db_name}")

engine.connect()
