import os

import dropbox
from django.utils.text import slugify

from apps.core.models import File

DROPBOX_TOKEN = os.getenv('DROPBOX_TOKEN')


def create_file(file):
    try:
        dbx = dropbox.Dropbox(DROPBOX_TOKEN)
        dbx.files_upload(file.read(), f'/{file.name}')
        file = File.objects.create(name=file.name, slug=slugify(file.name), file=f"/{file.name}")

    except dropbox.exceptions.ApiError as e:
        print(f"Error uploading file to Dropbox: {e}")
    return file


def generate_download_url(file_path_in_dropbox):
    try:
        dbx = dropbox.Dropbox(DROPBOX_TOKEN)
        download_url = dbx.files_get_temporary_link(file_path_in_dropbox).link
    except dropbox.exceptions.ApiError as e:
        print("Error getting temporary link:", e)
        return None

    return download_url


def file_delete(file):
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    dbx.files_delete_v2(file.file)
    file.delete()
