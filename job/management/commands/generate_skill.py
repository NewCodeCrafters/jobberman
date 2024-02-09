from django.core.management.base import BaseCommand
from faker import Faker
from job.models import Skill  # Update with your actual Skill model import


class Command(BaseCommand):
    help = 'Generates fake skills'

    def handle(self, *args, **options):
        fake = Faker()
        self.stdout.write("Generating Skills...")
        for _ in range(200):
            skill = Skill.objects.create(title=fake.job())
            skill.save()
            self.stdout.write(self.style.SUCCESS(f"{skill.title} created successfully..."))
        self.stdout.write(self.style.SUCCESS("Skills created successfully."))
