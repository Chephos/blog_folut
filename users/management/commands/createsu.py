import os
from pathlib import Path

from django.contrib.auth import  get_user_model
from django.core.management.base import BaseCommand

from dotenv import load_dotenv

User = get_user_model()
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')
class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password=os.getenv("ADMIN_PASSWORD"),
            )
        print('Superuser has been created.')