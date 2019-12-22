import uuid
from sqlalchemy import Column, Index, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates

from forum_service.db.models.base import BaseModelMixin
from forum_service.db.base import Base
from forum_service.db.types import Text, UTCDateTime


class ForumData(BaseModelMixin, Base):
    __tablename__ = 'forum_data'

    user_id = Column(UUID, ForeignKey('forum.id'), primary_key=True)
    subscriber_count = Column(Integer)
