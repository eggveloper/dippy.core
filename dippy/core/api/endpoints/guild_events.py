from __future__ import annotations
from typing import Optional
from dippy.core.datetime_helpers import datetime
from dippy.core.api.models.guilds import EventEntityMetadata
from dippy.core.api.request import RequestModel, QueryArgField, URLArgField, JSONArgField
from dippy.core.enums.guilds import EventPrivacyLevel, EventEntityType
from dippy.core.snowflake import Snowflake


class ListScheduledEventsForGuild(RequestModel):
    endpoint = "/guilds/{guild.id}/scheduled-events"
    method = "GET"

    guild_id: Snowflake = URLArgField(index=True)
    with_user_count: Optional[bool] = QueryArgField()

