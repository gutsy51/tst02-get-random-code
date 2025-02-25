from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic.base import View
from random import randint


def get_code():
    return (randint(0, 9) for _ in range(4))


class RandNumView(View):
    """ Random Number (4-digit code) View. """

    template_name = 'code-apps/code-no-auth.html'

    def get(self, request):
        context = {
            "digits": get_code(),
        }
        return render(request, self.template_name, context)


class RanNumAuthView(View):
    """ Random Number (4-digit code) View. """

    login_url = "auth:login"
    template_name = 'code-apps/code-auth.html'

    def get(self, request):
        context = {} if not request.user.is_authenticated else {"digits": get_code()}
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('code2')