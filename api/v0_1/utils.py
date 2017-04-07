def get_url(request, code):
    """
    Returns short URL by code
    """
    return '%s://%s/%s' % (
        request.scheme,
        request.get_host(),
        code, )
