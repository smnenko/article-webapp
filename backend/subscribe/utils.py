from authapp.models import User


def get_author_subscriber_ids_from_request(request):
    author, subscriber = None, None

    if 'author' in request.data:
        author = User.objects.filter(username=request.data['author']).first().id
    if 'author' in request.query_params:
        author = User.objects.filter(username=request.query_params['author']).first().id
    if 'subscriber' in request.data:
        subscriber = User.objects.filter(email=request.data['subscriber']).first().id
    if 'subscriber' in request.query_params:
        subscriber = User.objects.filter(email=request.query_params['subscriber']).first().id
    return author, subscriber
