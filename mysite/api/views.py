from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import EventSerializer,ProductSerializer,ExamSerializer
from api.paginations import CustomPagination
from training.models import Event,Product
from exam_certification.models import Exam
# Create your views here.



class GetProductList(APIView):
    pagination_class = CustomPagination
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        result = {
            "status": False,
            "msg": "Done"
        }
        eventList = Product.objects.all()
        page = self.paginate_queryset(eventList)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            eventSerializer = self.get_paginated_response(serializer.data)

        return Response(eventSerializer.data, status=status.HTTP_200_OK)



    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
             if self.pagination_class is None:
                 self._paginator = None
             else:
                 self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)



class GetProductByID(APIView):
    pagination_class = CustomPagination


    def get(self, request, *args,**kwargs):
        result = {}
        id = self.kwargs['id']
        print(id)
        product = Product.objects.filter(id=id).first()
        result['id'] = product.id
        result['name'] = product.name
        result['code'] = product.code
        result['price'] = product.price
        result['type'] = product.type
        result['categoryID'] = product.category.id
        result['category'] = product.category.title
        result['description'] = product.description

        return Response(result, status=status.HTTP_200_OK)






class GetExamList(APIView):
    pagination_class = CustomPagination
    serializer_class = ExamSerializer

    def get(self, request, format=None):
        result = {
            "status": False,
            "msg": "Done"
        }
        examList = Exam.objects.all()
        page = self.paginate_queryset(examList)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            examSerializer = self.get_paginated_response(serializer.data)

        return Response(examSerializer.data, status=status.HTTP_200_OK)



    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
             if self.pagination_class is None:
                 self._paginator = None
             else:
                 self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

