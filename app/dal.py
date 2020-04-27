# Data Access Layer
from enum import Enum
from typing import Any, List, Optional, Union
from datetime import datetime, date, timezone, timedelta

import databases
import sqlalchemy
from sqlalchemy import Table
from pydantic import BaseModel

from app import config


# DB & SQLA
db = databases.Database(config.DB_URL)
engine = sqlalchemy.create_engine(config.DB_URL)
dbmeta = sqlalchemy.MetaData()

# Tables
# EXAMPLE:
items = Table("items", dbmeta, autoload=True, autoload_with=engine)
# ...

class Item(BaseModel):
    id: int
    created_at: datetime
    posted_at: Optional[datetime]
    # ...


class EntitiesList(BaseModel):
    total: int
    offset: int
    limit: int
    entities: List[BaseModel]
    debug: Any

    class Config:
        fields = {"debug": "_debug"}


class ItemsList(EntitiesList):
    entities: List[Item]
