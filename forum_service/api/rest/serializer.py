import serpy


class ForumSerializer(serpy.Serializer):
    id = serpy.StrField()
    name = serpy.StrField()
    description = serpy.StrField()


class PostSerializer(serpy.Serializer):
    id = serpy.StrField()
    title = serpy.StrField()
    content = serpy.StrField()
    author_id = serpy.StrField()
    forum_id = serpy.Field()


class CommentSerializer(serpy.Serializer):
    id = serpy.StrField()
    email = serpy.StrField()
    username = serpy.StrField()
    email_verified_at = serpy.Field()
    deactivated_at = serpy.Field()
