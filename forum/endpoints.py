from ajax.exceptions import AJAXError

def right_back_at_you(request):
    if len(request.POST):
        return request.POST
    else:
        raise AJAXError(500, 'Nothing to echo back.')
