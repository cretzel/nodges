from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from nodgessite.nodges.models import Node, Edge

def map(request, node_id):
    node = get_object_or_404(Node, pk=node_id)
    parent_list = Node.objects.filter(outgoing_edges__to_node__id=node.id)
    child_list = Node.objects.filter(incoming_edges__from_node__id=node.id)

    return render_to_response("nodges/map.html", {
            'node': node,
            'parent_list': parent_list,
            'child_list': child_list,
            })

def view(request, node_id):
    node = get_object_or_404(Node, pk=node_id)
    parent_list = Node.objects.filter(outgoing_edges__to_node__id=node.id)
    child_list = Node.objects.filter(incoming_edges__from_node__id=node.id)

    return render_to_response("nodges/view.html", {
            'node': node,
            'parent_list': parent_list,
            'child_list': child_list,
            })

def update(request, node_id):
    node = get_object_or_404(Node, pk=node_id)
    new_title = request.POST['title']
    new_description = request.POST['description']
    if "" == new_title:
        parent_list = Node.objects.filter(outgoing_edges__to_node__id=node.id)
        child_list = Node.objects.filter(incoming_edges__from_node__id=node.id)
        return render_to_response("nodges/view.html", {
                'node': node,
                'parent_list': parent_list,
                'child_list': child_list,
                'error_message': "Title must not be empty", 
                })
    else:
        node.title = new_title
        node.description = new_description
        node.save()
        return HttpResponseRedirect(reverse('nodgessite.nodges.views.view', args=(node.id,)))
