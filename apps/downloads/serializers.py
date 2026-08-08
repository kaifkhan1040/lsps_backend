from rest_framework import serializers

from apps.downloads.models import DownloadCategory, DownloadDocument


class DownloadDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadDocument
        fields = ["id", "title", "file", "updated_at"]


class DownloadCategorySerializer(serializers.ModelSerializer):
    documents = serializers.SerializerMethodField()

    class Meta:
        model = DownloadCategory
        fields = ["id", "name", "order", "documents"]

    def get_documents(self, obj):
        active_docs = obj.documents.filter(is_active=True)
        return DownloadDocumentSerializer(active_docs, many=True, context=self.context).data
