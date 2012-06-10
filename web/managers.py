from django.db.models import Manager


class PublicManager(Manager):
    """Returns published featured teasers."""

    def published(self):
        return self.get_query_set().filter(status__gte=2)