from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from . import models
from . import serializer


class CourseCategoryView(GenericViewSet, ListModelMixin):
    queryset = models.CourseCategory.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializer.CourseCategorySerializer


from .paginations import PageNumberPagination

from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from .filters import MyFilter, CourseFilterSet


class CoursesView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializer.CourseModelSerializer
    pagination_class = PageNumberPagination

    # 过滤和排序
    # filter_backends = [DjangoFilterBackend,OrderingFilter, SearchFilter]
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    # filter_backends = OrderingFilter
    ordering_fields = ['id', 'price', 'students']
    # search_fields = ['name']
    filterset_fields = ['course_category']

    # # 通过django_filters扩展过滤
    # filter_backends = [DjangoFilterBackend]
    # # 原来是配置字段,现在是配置类
    # filterset_class = CourseFilterSet


'''
django-filters指定以某个字段过滤有两种方式
第一种:
    配置类:
    filter_backends = [DjangoFilterBackend, ] 
    配置字段:
    filterset_fields = ['course_category']
    
第二种:
    # 配置类
    filter_backends = [DjangoFilterBackend ]
    # 配置类(自己写的类)
        from django_filters.filterset import FilterSet
        from . import  models
        class CourseFilterSet(FilterSet):
            class Meta:
                model = models.Course
                fields =  ['course_category']
    filterset_class = CourseFilterSet  
    
第三次：实习那区间过滤
from django_filters.filterset import FilterSet
from django_filters import filters
from . import models

class CourseFilterSet(FilterSet):
    # 课程的价格范围要大于min_price,小于max_price
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = models.Course
        fields = ['course_category','min_price', 'max_price']
    # 配置类
    filter_backends = [DjangoFilterBackend ]
    # 配置类(自己写的类)
    filterset_class = CourseFilterSet  
    
'''

'''
排序：按id正序排序,按price正序倒叙排列
使用：http://127.0.0.1:8000/course/free/?ordering=-id
配置类:
    filter_backends = [OrderingFilter, ]
配置字段:
    ordering_fields = ['id', 'price']
    
内置过滤：
使用：http://127.0.0.1:8000/course/free/?search=39
按照price过滤(表自己有的字段直接过滤)
配置类:
    filter_backends = [SearchFilter, ] 
配置字段:
    search_fields = ['price']
扩展：django-filter
安装:
支持自有字段的过滤还支持外键字段的过滤
使用：http://127.0.0.1:8000/course/free/?course_category=1  # 过滤分类为1(python的所有课程)
配置类:
    filter_backends = [DjangoFilterBackend, ] 
配置字段:
    filterset_fields = ['course_category']
'''


# 自定义排序或者过滤类

# 课程章节接口
class CourseChapterView(GenericViewSet, ListModelMixin):
    queryset = models.CourseChapter.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializer.CourseChapterSerializer
    # 可以按照课程Id来查
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']


# 搜索接口
class CoursesSearchView(GenericViewSet, ListModelMixin, ):
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializer.CourseModelSerializer
    pagination_class = PageNumberPagination

    filter_backends = [SearchFilter]
    search_fields = ['name']
