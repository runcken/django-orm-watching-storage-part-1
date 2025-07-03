import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


if __name__ == '__main__':
    print('Всего пропусков', Passcard.objects.count())
    print('Активных пропусков', len(Passcard.objects.filter(is_active=True)))
