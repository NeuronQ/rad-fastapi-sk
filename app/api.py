from typing import Optional

from fastapi import Request, APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse, RedirectResponse

from app import config
from app.auth import (
    User,
    get_current_active_api_read_user,
)
from app.dal import (
    db,
    items,
    articles,
    Article_with_Item_dataList,
    ItemsList,
    NewsList,
)
from app.alogic import (
    get_table_counts,
    get_items_list,
    get_articles_list,
    get_mixed_news_from_items_list,
    get_twitter_news_from_articles_list,
)


router = APIRouter()


@router.get("/users/self", response_model=User)
async def users_self(user: User = Depends(get_current_active_api_read_user)):
    return user


count_responses = {
    200: {
        "description": "Total Count",
        "content": {"application/json": {"example": {"total": 101}}},
    },
    2001: {
        "description": "Counts by Column",
        "content": {
            "application/json": {"example": {"<by column name>": "foo", "count": 42}}
        },
    },
}


@router.get("/items/count", responses=count_responses)
async def items_count(
    by: Optional[str] = None, user: User = Depends(get_current_active_api_read_user)
):
    return await get_table_counts(items, by)


@router.get("/items", response_model=ItemsList)
async def items_list(
    when: str = Query(
        ..., regex=r"^today|this-week$", description="Values: `today` | `this-week`"
    ),
    utc_offset_h: int = 0,
    limit: int = 100,
    offset: int = 0,
    dchan_type: Optional[str] = Query(
        None,
        regex=r"^(feed|twitter_filter|reddit)(,(feed|twitter_filter|reddit))*$",
        description="Values: comma separated list of values from: `feed`,`twitter_filter`,`reddit`",
    ),
    dchan_tags: Optional[str] = None,
    user: User = Depends(get_current_active_api_read_user),
):
    return await get_items_list(
        when, utc_offset_h, limit, offset, dchan_type, dchan_tags
    )
