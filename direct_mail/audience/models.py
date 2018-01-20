from django.db import models
from treebeard.ns_tree import NS_Node

# Create your models here.
class Audience(NS_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __unicode__(self):
        return 'Audience: %s' % self.name
