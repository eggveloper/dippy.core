from __future__ import annotations
from typing import Optional
from dippy.core.datetime_helpers import datetime
from dippy.core.api.models.guilds import EventEntityMetadata
from dippy.core.api.request import RequestModel, QueryArgField, URLArgField, JSONArgField
from dippy.core.enums.guilds import EventPrivacyLevel, EventEntityType, EventStatus
from dippy.core.snowflake import Snowflake


class ListScheduledEventsForGuild(RequestModel):
    endpoint = "/guilds/{guild.id}/scheduled-events"
    method = "GET"

    guild_id: Snowflake = URLArgField(index=True)
    with_user_count: Optional[bool] = QueryArgField()


class CreateGuildScheduledEvent(RequestModel):
    endpoint = "/guilds/{guild.id}/scheduled-events"
    method = "GET"

    guild_id: Snowflake = URLArgField(index=True)
    channel_id: Optional[Snowflake] = JSONArgField()
    entity_metadata: Optional[EventEntityMetadata] = JSONArgField()
    name: str = JSONArgField()
    privacy_level: EventPrivacyLevel = JSONArgField()
    scheduled_start_time: datetime = JSONArgField()
    scheduled_end_time: Optional[datetime] = JSONArgField()
    description: Optional[str] = JSONArgField()
    entity_type: EventEntityType = JSONArgField()


class GetGuildScheduledEvent(RequestModel):
    endpoint = "/guilds/{guild.id}/scheduled-events/{guild_scheduled_event.id}"
    method = "GET"

    with_user_count: Optional[bool] = QueryArgField(index=True)

class ModifyGuildScheduledEvent(RequestModel):
    endpoint = "/guilds/{guild.id}/scheduled-events/{guild_scheduled_event.id}"
    method = "PATCH"

    guild_id: Snowflake = URLArgField(index=True)
    guild_scheduled_event_id: Snowflake = URLArgField(index=True)

    channel_id: Optional[Snowflake] = JSONArgField()
    entity_metadata: Optional[EventEntityMetadata] = JSONArgField()
    name: Optional[str] = JSONArgField()
    privacy_level: Optional[EventPrivacyLevel] = JSONArgField()
    scheduled_start_time: Optional[datetime] = JSONArgField()
    scheduled_end_time: Optional[datetime] = JSONArgField()
    description: Optional[str] = JSONArgField()
    entity_type: Optional[EventEntityType] = JSONArgField()
    status: Optional[EventStatus] = JSONArgField()





