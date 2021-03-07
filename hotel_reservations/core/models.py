from uuid import uuid4

from django.db import models
from django.utils import timezone
from django_lifecycle import LifecycleModelMixin


class UUIDidentifier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


class BaseModel(UUIDidentifier, LifecycleModelMixin):

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True

    @property
    def changed(self):
        return True if self.modified else False

    def save(self, *args, **kwargs):
        if self.pk:
            self.modified = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)
