import logging
from datetime import date
from enum import Enum

from pydantic import BaseModel, BeforeValidator
from typing_extensions import Annotated

logger = logging.getLogger(__name__)


def ensure_tuple(created: str | tuple) -> tuple:
    if isinstance(created, str):
        return tuple(created.split(", "))
    return created


class SampleSchema(BaseModel):
    id: str
    text: str
    source: str
    added: date
    created: Annotated[tuple[date, date], BeforeValidator(ensure_tuple)]
    token_count: int


class ColumnNames(Enum):
    id = "id"
    text = "text"
    source = "source"
    added = "added"
    created = "created"
    token_count = "token_count"


COLUMN_ORDER = [col.value for col in ColumnNames]
