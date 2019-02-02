# Compatible with Python2 and Python3
try:
    from urllib.parse import urljoin # Python3
except ImportError:
    from urlparse import urljoin # Python2

from django.views.generic.base import RedirectView


class FaviconView(RedirectView):
    """
    Redirects to the favicon from the LMS
    """
    def get_redirect_url(self, *_args, **_kwargs):
        site_configuration = self.request.site.siteconfiguration
        if not site_configuration.homepage_url:
            return None
        return urljoin(site_configuration.homepage_url, '/favicon.ico')
