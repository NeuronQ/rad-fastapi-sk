from datetime import datetime, timedelta, timezone
import sqlparse


def query_to_str(query, engine):
    return str(query.compile(engine)).replace("\n", " ")


def query_to_formatted_str(query, engine):
    return sqlparse.format(query_to_str(query, engine), reindent=True, keyword_case='upper')


def start_of_today(utc_offset_h: int = 0) -> datetime:
    tz = timezone(timedelta(hours=utc_offset_h))
    now_at_tz = datetime.now(tz=tz)
    return datetime(now_at_tz.year, now_at_tz.month, now_at_tz.day)


def start_of_this_week(utc_offset_h: int = 0) -> datetime:
    tz = timezone(timedelta(hours=utc_offset_h))
    now_at_tz = datetime.now(tz=tz).replace(hour=0, minute=0)
    start_of_week = now_at_tz - timedelta(days=now_at_tz.weekday())
    # start_of_week = now_at_tz - timedelta(days=30)  # DEBUG
    return datetime(start_of_week.year, start_of_week.month, start_of_week.day)
