import uuid
from sqlalchemy import Column, Index, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates

from forum_service.db.models.base import BaseModelMixin
from forum_service.db.base import Base
from forum_service.db.types import Text, UTCDateTime


class Post(BaseModelMixin, Base):
    __tablename__ = 'post'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(Text)
    content = Column(Text)
    author_id = Column(UUID, nullable=False)
    forum_id = Column(UUID, ForeignKey('forum.id'))
    forum = relationship("Forum", back_populates="posts")
