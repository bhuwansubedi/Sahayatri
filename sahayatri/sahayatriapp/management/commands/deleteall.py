from lib2to3.pytree import Base
from django.core.management.base import BaseCommand

from sahayatriapp.management.commands.addaddress import Command
from ...models import Municipality,District,Province


class Command(BaseCommand):
    Province.objects.all().delete()
    Municipality.objects.all().delete()
    District.objects.all().delete()