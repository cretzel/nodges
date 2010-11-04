from django.db import models

class Node(models.Model):
    title = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

class Edge(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    from_node = models.ForeignKey(Node, verbose_name='from_node', related_name='outgoing_edges')
    to_node = models.ForeignKey(Node, verbose_name='to_node', related_name='incoming_edges')

    def __unicode__(self):
        return "%s [%s -> %s]" % (self.title, self.from_node, self.to_node)

