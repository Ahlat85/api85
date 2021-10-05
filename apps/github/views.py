import requests

from django.http import HttpResponse

from django.views import View

class FileView(View):
  __github = 'https://raw.githubusercontent.com'
  
  def get(self ,request, *args, **kwargs):
    username = kwargs['username']
    repo = kwargs['repo']
    branch_or_tag = kwargs['branch_or_tag']
    file_name = kwargs['file_name'].replace('|', '/')
    
    url = f'{self.__github}/{username}/{repo}/{branch_or_tag}/{file_name}'
    
    send = requests.get(url)
    if send.status_code == 200:
      result = send
    else:
      result = f'File on "{url}" is not found!'
      
    return HttpResponse(result)