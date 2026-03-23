"""
Management command: create_superuser_if_not_exists

Creates the admin superuser on first deploy using environment variables.
Safe to run on every deploy — skips if the user already exists.

Env vars (all optional, sensible defaults provided):
  DJANGO_SUPERUSER_USERNAME  default: admin
  DJANGO_SUPERUSER_EMAIL     default: admin@in16.ac.ke
  DJANGO_SUPERUSER_PASSWORD  default: admin123
"""
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create a superuser if one does not already exist."

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@in16.ac.ke")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(
                f"Superuser '{username}' already exists — skipping."
            ))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(
            f"Superuser '{username}' created successfully."
        ))
