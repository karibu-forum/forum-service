import uuid
from sqlalchemy import Column, Index, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates

from forum_service.db.models.base import BaseModelMixin
from forum_service.db.base import Base
from forum_service.db.types import Text, UTCDateTime


class PostData(BaseModelMixin, Base):
    __tablename__ = 'post_data'

    post_id = Column(UUID, ForeignKey('post.id'), primary_key=True)
    up_vote = Column(Integer)
    down_vote = Column(Integer)