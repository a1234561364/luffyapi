
from django.urls import path,re_path,include
from . import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('categories',views.CourseCategoryView,'categories')
router.register('free',views.CoursesView,'free')
router.register('chapters',views.CourseChapterView,'chapters')
router.register('search',views.CoursesSearchView,'search')

urlpatterns = [
    path('', include(router.urls)),
]
