"""
Definition of models.
"""

from django.db import models
import json

class StarredRepo(models.Model):
    full_name = models.CharField(max_length=200)
    html_url = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.full_name

    def __init__(self, json_def):
        self.__dict__ = json.loads(json.dumps(json_def))

