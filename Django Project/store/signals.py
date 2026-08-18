# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from .models import Product

# @receiver(post_save, sender=Product)
# def set_quantity(instance, sender, created, **kwargs):
#     if created:
#         instance.quantity = 10
#         instance.save(update_fields=['quantity'])