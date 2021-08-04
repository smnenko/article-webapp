from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import View

from authapp.models import User
from article.models import Article


class IsAuthor(BasePermission):

    def has_permission(self, request: Request, view: View):
        return Article.objects.filter(
            pk=view.kwargs.get('pk'),
            author__email=request.query_params.get('author')
        ).exists()
