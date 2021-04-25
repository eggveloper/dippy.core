from enum import Enum, IntEnum


class StrEnum(str, Enum):
    ...


class GatewayCode(IntEnum):
    # An event was dispatched.
    DISPATCH = 0
    # Fired periodically by the client to keep the connection alive.
    HEARTBEAT = 1
    # Starts a new session during the initial handshake.
    IDENTIFY = 2
    # Update the client's presence.
    PRESENCE_UPDATE = 3
    # Used to join/leave or move between voice channels.
    VOICE_STATE_UPDATE = 4
    # Resume a previous session that was disconnected.
    RESUME = 6
    # You should attempt to reconnect and resume immediately.
    RECONNECT = 7
    # Request information about offline guild members in a large guild.
    REQUEST_GUILD_MEMBERS = 8
    # The session has been invalidated. You should reconnect and identify/resume accordingly.
    INVALID_SESSION = 9
    # Sent immediately after connecting, contains the heartbeat_interval to use.
    HELLO = 10
    # Sent in response to receiving a heartbeat to acknowledge that it has been received.
    HEARTBEAT_ACK = 11


class ChannelType(IntEnum):
    TEXT = 0
    DM = 1
    VOICE = 2
    GROUP_DM = 3
    CATEGORY = 4
    NEWS = 5
    STORE = 5
    STAGE = 13


class OverwriteType(StrEnum):
    ROLE = "role"
    MEMBER = "member"


class Status(StrEnum):
    ONLINE = "online"
    OFFLINE = "offline"
    DND = "dnd"
    IDLE = "idle"


class MembershipState(IntEnum):
    INVITED = 1
    ACCEPTED = 1


class EmbedType(StrEnum):
    RICH = "rich"
    IMAGE = "image"
    VIDEO = "video"
    GIFV = "gifv"
    ARTICLE = "article"
    LINK = "link"


class MessageType(IntEnum):
    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    GUILD_MEMBER_JOIN = 7
    USER_PREMIUM_GUILD_SUBSCRIPTION = 8
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_1 = 9
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_2 = 10
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    REPLY = 19
    APPLICATION_COMMAND = 20
    GUILD_INVITE_REMINDER = 22


class MessageActivityType(IntEnum):
    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 5


class MessageFlags(IntEnum):
    # This message has been published to subscribed channels (via Channel Following)
    CROSSPOSTED = 1 << 0
    # This message originated from a message in another channel (via Channel Following)
    IS_CROSSPOST = 1 << 1
    # Do not include any embeds when serializing this message
    SUPPRESS_EMBEDS = 1 << 2
    # The source message for this crosspost has been deleted (via Channel Following)
    SOURCE_MESSAGE_DELETED = 1 << 3
    # This message came from the urgent message system
    URGENT = 1 << 4
    # This message is only visible to the user who invoked the Interaction
    EPHEMERAL = 1 << 6
    # This message is an Interaction Response and the bot is "thinking"
    LOADING = 1 << 7


class StickerFormatType(IntEnum):
    PNG = 1
    APNG = 2
    LOTTIE = 3


class InteractionResponseType(IntEnum):
    # ACK a Ping
    PONG = 1
    # DEPRECATED ACK a command without sending a message, eating the user's input
    ACKNOWLEDGEMENT = 2
    # DEPRECATED respond with a message, eating the user's input
    CHANNEL_MESSAGE = 3
    # respond to an interaction with a message
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    # ACK an interaction and edit a response later, the user sees a loading state
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5


class ActivityType(IntEnum):
    GAME = 0
    STREAMING = 1
    LISTENING = 2
    WATCHING = 3
    CUSTOM = 4
    COMPETING = 5


class ActivityFlag(IntEnum):
    INSTANCE = 1 << 0
    JOIN = 1 << 1
    SPECTATE = 1 << 2
    JOIN_REQUEST = 1 << 3
    SYNC = 1 << 4
    PLAY = 1 << 5


class ApplicationCommandOptionType(IntEnum):
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8


class InteractionType(IntEnum):
    PING = 1
    APPLICATION_COMMAND = 2


class VerificationLevel(IntEnum):
    NONE = 0  # Unrestricted
    LOW = 1  # Must have verified email on account
    MEDIUM = 2  # Must be registered on Discord for longer than 5 minutes
    HIGH = 3  # Must be a member of the server for longer than 10 minutes
    VERY_HIGH = 4  # Must have a verified phone number


class DefaultMessageNotificationLevel(IntEnum):
    ALL_MESSAGES = 0  # Members will receive notifications for all messages by default
    ONLY_MENTIONS = 1  # Members will receive notifications only for messages that @mention them by default


class ExplicitContentFilterLevel(IntEnum):
    # Media content will not be scanned
    DISABLED = 0
    # Media content sent by members without roles will be scanned
    MEMBERS_WITHOUT_ROLES = 1
    # Media content sent by all members will be scanned
    ALL_MEMBERS = 2
