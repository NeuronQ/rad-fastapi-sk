from math import ceil
from typing import Any, List, Mapping, Optional, Union

from sqlalchemy import desc, func, Table
from sqlalchemy.sql import select, and_, or_, not_

from fastapi import HTTPException

from app.helpers import query_to_str, start_of_this_week, start_of_today
from app.dal import (
    db,
    engine,
    items,
    ItemsList,
)


# Application and Domain logic goes here
