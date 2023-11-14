from django.test import TestCase
from uploadapp.models import File, ImageFile

# Create your tests here.


class ImageFileModelTestCase(TestCase):
    def test_imagefile_creation(self):
        image_file_instance = ImageFile.objects.create(
            img_file="/uploads/images/logo.png")
        print(image_file_instance.img_file)
        self.assertEqual(image_file_instance.img_file.name,
                         '/uploads/images/logo.png')
