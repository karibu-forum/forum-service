import uuid
from sqlalchemy import Column, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates

from forum_service.db.models.base import BaseModelMixin
from forum_service.db.base import Base
from forum_service.db.types import Text, UTCDateTime


class Forum(BaseModelMixin, Base):
    __tablename__ = 'forum'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, unique=True)
    description = Column(Text)
    posts = relationship("Post")
