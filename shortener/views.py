from django.views.generic.base import RedirectView

from models import Link


class GoToLinkView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        """
        Return the URL redirect to.
        """
        try:
            instance = Link.objects.get(pk=kwargs.get('code'))
        except Link.DoesNotExist:
            return None
        instance.qty += 1
        instance.save()
        return instance.url
