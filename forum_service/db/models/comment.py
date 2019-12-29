import uuid
from sqlalchemy import Column, Index, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates

from forum_service.db.models.base import BaseModelMixin
from forum_service.db.base import Base
from forum_service.db.types import Text, UTCDateTime


class Comment(BaseModelMixin, Base):
    __tablename__ = 'comment'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text)
    author_id = Column(UUID, nullable=False)
    post_id = Column(UUID, ForeignKey('post.id'))
    last_edited_at = Column(UTCDateTime)
    post = relationship("Post", back_populates="posts")  #  Not quite right
