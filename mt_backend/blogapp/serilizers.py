from rest_framework import serializers
from blogapp.models import Comment, Blog

# Write serializers here


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)

    def get_uploaded_by(self, obj):
        return f"{obj.uploaded_by.first_name} {obj.uploaded_by.last_name}"

    class Meta:
        model = Blog
        fields = "__all__"
