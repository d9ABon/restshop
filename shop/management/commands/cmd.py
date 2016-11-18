# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from optparse import make_option
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _


class Command(BaseCommand):
    help = _("test")

    def add_arguments(self, parser):
        parser.add_argument("--custom_arg", action='store_true', dest='custom_arg',
            help=_("optional arg"))

    def handle(self, verbosity, custom_arg, *args, **options):

        from django.core.cache import cache
        cache.set('aaa', 'bbb', 60)
        print cache.get('aaa')

        self.stdout.write('DONE')
