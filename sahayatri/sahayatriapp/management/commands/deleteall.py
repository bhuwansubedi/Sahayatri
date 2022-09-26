from lib2to3.pytree import Base
from django.core.management.base import BaseCommand

from sahayatriapp.management.commands.addaddress import Command
from ...models import Bucketlist, Municipality,District, Order,Province


class Command(BaseCommand):
    Order.objects.all().delete()
    Bucketlist.objects.all().delete()    