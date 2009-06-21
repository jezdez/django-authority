from django.contrib.flatpages.views import flatpage
from django.contrib.flatpages.models import FlatPage

from authority.decorators import permission_required

@permission_required('flatpage_permission.top_secret', (FlatPage, 'url__contains'))
def top_secret(request, url):
    """
    A wrapping view that performs the permission check given in the decorator
    """
    print "secret!"
    return flatpage(request, url)
