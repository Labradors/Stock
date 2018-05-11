import sys
import os
import django

sys.path.append('../../../stock')
os.environ['DJANGO_SETTINGS_MODULE'] = 'stock.settings'
django.setup()