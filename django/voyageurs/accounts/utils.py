from django.db.models import Count
from persons.models import Person
from datetime import datetime
from django.db.models import Q


def get_user_total_counter(user):
    total = Person.objects.filter(collector=user).count()
    return total

def get_user_daily_counter(user):
    today = datetime.today().date()
    daily = Person.objects.filter(date_saisie__date=today, collector=user).count()
    return daily