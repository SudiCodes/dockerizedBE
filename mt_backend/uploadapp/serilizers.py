from rest_framework import serializers
import magic
from uploadapp.models import File, ImageFile


class FileSerilizer(serializers.ModelSerializer):
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB in bytes
    ALLOWED_TYPES = ["application/pdf", "text/plain"]

    class Meta:
        model = File
        fields = "__all__"

    def validate_file(self, value):
        # Check file size
        if value.size > self.MAX_FILE_SIZE:
            raise serializers.ValidationError("File size exceeds 10MB")

        # Identify file type based on content
        mime = magic.Magic(mime=True)
        file_content = value.read()
        detected_mime_type = mime.from_buffer(file_content)
        print(detected_mime_type)

        # Check detected MIME type
        if detected_mime_type not in self.ALLOWED_TYPES:
            raise serializers.ValidationError(
                "Only PDF and text (TXT) files are allowed")

        return value


class ImageFileSerializer(serializers.ModelSerializer):
    MAX_FILE_SIZE = 1 * 1024 * 1024  # 2MB in bytes
    ALLOWED_TYPES = ["image/jpeg", "image/png"]

    class Meta:
        model = ImageFile
        fields = "__all__"

    def validate_file(self, value):
        print(value.size)
        try:
            if value.size > self.MAX_FILE_SIZE:
                raise serializers.ValidationError(
                    "File size exceeds maximum allowed")

            detected_mime_type = self.get_file_mime_type(value)

            if detected_mime_type not in self.ALLOWED_TYPES:
                raise serializers.ValidationError(
                    "Only JPEG and PNG files are allowed")

            return value
        except Exception as e:
            raise serializers.ValidationError("Invalid file")
        finally:
            value.close()

    def get_file_mime_type(self, file):
        with magic.Magic(mime=True) as mime:
            file_content = file.read()
            detected_mime_type = mime.from_buffer(file_content)
            file.seek(0)  # Reset file pointer after reading content
            return detected_mime_type
