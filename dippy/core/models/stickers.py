from __future__ import annotations
from attr import attrs
from dippy.core.enums.stickers import StickerType, StickerFormatType
from dippy.core.models.users import User
from dippy.core.snowflake import Snowflake
from typing import Optional


@attrs(auto_attribs=True)
class Sticker:
    id: Snowflake
    pack_id: Optional[Snowflake]
    name: str
    description: Optional[str]
    tags: str
    type: StickerType
    format_type: StickerFormatType
    available: Optional[bool]
    guild_id: Optional[Snowflake]
    user: Optional[User]
    sort_value: Optional[int]
