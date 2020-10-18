from django.db import models

# Not added as part of the model to
# prevent recreating always upon new
# model create.
STATUSES = [
    (0, 'NEW'),
    (1, 'STARTED'),
    (2, 'COMPLETED'),
]

class Todo(models.Model):
    title = models.CharField(max_length=50)
    status = models.IntegerField(default=0, choices=STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.get_status_display().title()})'
