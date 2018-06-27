from django.shortcuts import render
from django.views.generic import TemplateView

from SocialNetworkMerger.settings import instagram_access_token

import requests

class MediaLook(TemplateView):
    template_name = 'foreignapi/medialook_home.html'
    base_instagram_uri = 'https://api.instagram.com/v1/users/{user_id}/media/recent/' + \
                         '?access_token={access_token}'.format(access_token=instagram_access_token)

    def get(self, request, *args, **kwargs):
        instagram_id = request.GET.get('instagram_id')
        print(instagram_id)
        vk_id = request.GET.get('vk_id')
        images = []
        if instagram_id:
            url = self.base_instagram_uri.format(user_id=instagram_id)
            res = requests.get(url=url).json()
            for l in res['data']:
                if l.get('carousel_media'):
                    image_link = l['link']
                    for hop in l['carousel_media']:
                        if hop.get('images'):
                            image_url = hop['images']['standard_resolution']['url']
                            image = {
                                'image_link': image_link,
                                'image_url': image_url,
                            }
                            images.append(image)
                else:
                    if not l.get('videos'):
                        image_link = l['link']
                        image_url = l['images']['standard_resolution']['url']
                        image = {
                            'image_link': image_link,
                            'image_url': image_url,
                        }
                        images.append(image)
        args = {
            'images': images,
        }
        return render(request, self.template_name, args)

    def post(self, request):
        return render(request, self.template_name)
