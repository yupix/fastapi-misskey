from typing import Any, List, Optional
from pydantic import BaseModel
from pydantic.fields import Field


class User(BaseModel):
    id: str
    name: Any
    username: str
    host: Any
    avatar_url: str = Field(..., alias='avatarUrl')
    avatar_blurhash: str = Field(..., alias='avatarBlurhash')
    avatar_color: Any = Field(..., alias='avatarColor')
    is_admin: bool = Field(..., alias='isAdmin')
    is_bot: bool = Field(..., alias='isBot')
    is_cat: bool = Field(..., alias='isCat')
    is_lady: Optional[bool] = Field(False, alias='isLady')
    is_verified: Optional[bool] = Field(False, alias='isVerified')
    is_premium: Optional[bool] = Field(False, alias='isPremium')
    emojis: List
    has_unread_specified_notes: bool = Field(..., alias='hasUnreadSpecifiedNotes')
    has_unread_mentions: bool = Field(..., alias='hasUnreadMentions')
    online_status: str = Field(..., alias='onlineStatus')
    url: Any
    uri: Any
    created_at: str = Field(..., alias='createdAt')
    updated_at: str = Field(..., alias='updatedAt')
    banner_url: Any = Field(..., alias='bannerUrl')
    banner_blurhash: Any = Field(..., alias='bannerBlurhash')
    banner_color: Any = Field(..., alias='bannerColor')
    is_locked: bool = Field(..., alias='isLocked')
    is_moderator: bool = Field(..., alias='isModerator')
    is_silenced: bool = Field(..., alias='isSilenced')
    is_suspended: bool = Field(..., alias='isSuspended')
    description: Any
    location: Any
    birthday: Any
    fields: List
    followers_count: int = Field(..., alias='followersCount')
    following_count: int = Field(..., alias='followingCount')
    notes_count: int = Field(..., alias='notesCount')
    pinned_note_ids: List = Field(..., alias='pinnedNoteIds')
    pinned_page_id: Any = Field(..., alias='pinnedPageId')
    pinned_page: Any = Field(..., alias='pinnedPage')
    two_factor_enabled: bool = Field(..., alias='twoFactorEnabled')
    use_password_less_login: bool = Field(..., alias='usePasswordLessLogin')
    security_keys: bool = Field(..., alias='securityKeys')
    twitter: Any
    github: Any
    discord: Any
    avatar_id: str = Field(..., alias='avatarId')
    banner_id: Any = Field(..., alias='bannerId')
    auto_watch: Optional[bool] = Field(False, alias='autoWatch')
    always_mark_nsfw: bool = Field(..., alias='alwaysMarkNsfw')
    careful_bot: bool = Field(..., alias='carefulBot')
    careful_massive: Optional[bool] = Field(False, alias='carefulMassive')
    auto_accept_followed: bool = Field(..., alias='autoAcceptFollowed')
    no_crawle: bool = Field(..., alias='noCrawle')
    is_explorable: bool = Field(..., alias='isExplorable')
    is_deleted: bool = Field(..., alias='isDeleted')
    hide_online_status: bool = Field(..., alias='hideOnlineStatus')
    has_unread_announcement: bool = Field(..., alias='hasUnreadAnnouncement')
    has_unread_antenna: bool = Field(..., alias='hasUnreadAntenna')
    has_unread_channel: bool = Field(..., alias='hasUnreadChannel')
    has_unread_messaging_message: bool = Field(..., alias='hasUnreadMessagingMessage')
    has_unread_notification: bool = Field(..., alias='hasUnreadNotification')
    pending_received_follow_requests_count: Optional[bool] = Field(
        False, alias='pendingReceivedFollowRequestsCount'
    )
    muting_notification_types: List = Field(..., alias='mutingNotificationTypes')
