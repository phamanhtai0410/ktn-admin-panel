from datetime import datetime

import boto3
from flask_admin.form.upload import FileUploadField, ImageUploadInput, ImageUploadField
from src.config import Config


class CustomViewImageWidget(ImageUploadInput):
    data_template = ('<div>'
                     ' Current: <img style="width: 250px;"  %(image)s>'
                     '</div>'
                     '<input class="image_preview" %(file)s>')
    empty_template = '<input class="image_preview" %(file)s>'
    def get_url(self, field):
        return field.data


class S3ImageUploadField(FileUploadField):


    def __init__(self, *args, **kwargs):
        super(S3ImageUploadField, self).__init__(*args, **kwargs)

    widget = CustomViewImageWidget()

    # Deletion
    def _delete_file(self, filename):
        # super(ImageUploadField, self)._delete_file(filename)

        # self._delete_thumbnail(filename)
        pass


    # Saving
    def _save_file(self, data, filename):
        savedUrl = self._save_image(data, filename)
        return savedUrl

    def _save_image(self, image, path):
        s3 = boto3.client(
            "s3",
            endpoint_url=Config.S3_HOST,
            aws_access_key_id=Config.AWS_KEY,
            aws_secret_access_key=Config.AWS_SECRET,
            use_ssl=False
        )
        name_prefix = datetime.today().strftime('%hh%MM%ss')

        key_path_upload = f'{name_prefix}_{image.filename}'
        s3.upload_fileobj(
            image,
            Config.BUCKET_NAME,
            key_path_upload,
            ExtraArgs={
                "ContentType": image.content_type  # Set appropriate content type as per the file
            }
        )
        return f'{Config.S3_STATIC}/{name_prefix}_{image.filename}'
