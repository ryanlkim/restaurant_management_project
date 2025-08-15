from django.db.models.signals import post_migrate
from django.dispatch import receiver
from home.models import Restaurant

@receiver(post_migrate)
def create_restaurant(sender, **kwargs):
    if sender.name == 'home' and not Restaurant.objects.exists():
        Restaurant.objects.create(
            name="Restaurant Name",
            description="Placeholder description"
        )