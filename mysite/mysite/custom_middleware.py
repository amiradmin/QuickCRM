from monitoring.models import UserMonitor
from datetime import datetime
from django.conf import settings
from django.contrib.sites.models import Site
import re

compiledLists = {}
class LastActivityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("custom middleware before next middleware/view")
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        print(request.user.username)
        activeuser= UserMonitor.objects.filter(user = request.user)
        if activeuser.count() > 0 :
            activeuser=activeuser.first()
            activeuser.login_date = datetime.now()
            activeuser.save()
        else:
            activeuser = UserMonitor()
            activeuser.user = request.user
            activeuser.login_date = datetime.now()
            activeuser.save()

        # Code to be executed for each response after the view is called
        #
        print("custom middleware after response or previous middleware")

        return response


