from .settings import PORTAL_URL

def students_proc(request):
#  return {'PORTAL_URL': PORTAL_URL}
   return {'PORTAL_URL': request.scheme + '://'+ request.get_host()}
