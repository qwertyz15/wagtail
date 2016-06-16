from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore.models import Site
from wagtail.wagtailcore.request_cache import RequestCache


class SiteMiddleware(object):

    def process_request(self, request):
        """
        Set request.site to contain the Site object responsible for handling this request,
        according to hostname matching rules
        """
        try:
            request.site = Site.find_for_request(request)
        except Site.DoesNotExist:
            request.site = None


class RequestCacheMiddleware(object):
    """
    Creates a fresh cache instance as request.cache. The cache instance lives only as long as request does.
    """

    def process_request(self, request):
        request.cache = RequestCache()
