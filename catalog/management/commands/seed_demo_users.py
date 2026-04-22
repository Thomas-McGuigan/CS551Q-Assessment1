from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a couple of demo users for the login."

    def handle(self, *args, **options):
        user_model = get_user_model()
        created = 0

        for username in ("johnmovielover", "janemovielover"):
            user, was_created = user_model.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@example.com"},
            )
            user.set_password("ilovemovies")
            user.save()
            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Demo users ready. {created} created. Use johnmovielover/ilovemovies or janemovielover/ilovemovies."
            )
        )
