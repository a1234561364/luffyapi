from .celery import app


# cache
# model,serilizer


@app.task
def banner_update():
    # # 加载django环境
    # import os
    # import django
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffyapi.settings.dev")
    # django.setup()
    from home import serializer
    from home import models
    from django.conf import settings
    from django.core.cache import cache
    queryset_banner = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('display_order')[
                      :settings.BANNER_COUNTER]
    serializer_banner = serializer.BannerModelSerializers(instance=queryset_banner, many=True)
    # print(serializer_banner.data)
    for banner in serializer_banner.data:
        banner['img'] = 'http://127.0.0.1:8000' + banner['img']
    cache.set('banner_list', serializer_banner.data)
    # import time
    # time.sleep(1)
    # banner_list = cache.get('banner_list')
    # print(banner_list)


    # banner_list = cache.get('banner_list')
    # print(banner_list)
    return True
