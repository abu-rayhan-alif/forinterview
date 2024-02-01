from django.core.management.base import BaseCommand
from .models import create_groups

class Command(BaseCommand):
    help = 'Create default user groups'

    def handle(self, *args, **options):
        create_groups()
        self.stdout.write(self.style.SUCCESS('Successfully created default user groups.'))