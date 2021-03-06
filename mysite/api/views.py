from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import EventSerializer,ProductSerializer,ExamSerializer,EventSerializer
from api.paginations import CustomPagination
from training.models import Event,Product,productCategory,Event
from contacts.models import Contact
from scheduler.tasks import cerExpiration
from django.db.models import Q
import datetime
# Create your views here.





class TaskControl(APIView):
    def get(self, request, format=None):
        result = {
            "status": False,
            "msg": "Done"
        }
        cerExpiration.apply_async((5, 10), countdown=60)
        result['status'] = True
        result['msg'] = "Tasks started!"
        return Response(result, status=status.HTTP_200_OK)


class NewContact(APIView):

    def post(self, request, format=None):
        result = {
            "status": False,
            "msg": "Done"
        }
        data = request.data

        print("Contact Api")
        print(data)
        email = data['email']
        subject = data['subject']
        description = data['description']

        contact = Contact()
        contact.message = description
        contact.formName = email
        contact.type = "Site"
        contact.messageType = "Site"
        contact.save()
        print(email)
        result['email'] = email
        result['subject'] = subject
        result['description'] = description
        result['status'] = True
        result['msg'] = "contact has save successfully"
        return Response(result, status=status.HTTP_200_OK)




class GetProductList(APIView):
    pagination_class = CustomPagination
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        result = {
            "status": False,
            "msg": "Done"
        }
        eventList = Product.objects.filter(visible=True)
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
        result['title'] = product.title
        result['description'] = product.description
        result['code'] = product.code
        result['price'] = product.price
        result['type'] = product.type
        result['link'] = product.link
        result['categoryID'] = product.category.id
        result['category'] = product.category.title
        result['description'] = product.description
        if product.pic:
            result['image'] = 'http://erp.tescan.ca' + product.pic.url
        else:
            result['image'] = None
        return Response(result, status=status.HTTP_200_OK)



class GetEventByID(APIView):
    pagination_class = CustomPagination


    def get(self, request, *args,**kwargs):
        result = {}
        id = self.kwargs['id']
        print(id)
        product= Product.objects.filter(id=id).first()
        event = Event.objects.filter(product=product)
        result['id'] = product.id
        result['name'] = product.name
        result['code'] = product.code
        result['price'] = product.price
        result['type'] = product.type
        result['categoryID'] = product.category.id
        result['category'] = product.category.title

        return Response(result, status=status.HTTP_200_OK)




class GetExamList(APIView):
    pagination_class = CustomPagination
    serializer_class = EventSerializer

    def get(self, request, format=None):
        result = {
            "status": False,
            "msg": "Done"
        }
        # examList = Event.objects.filter(name= 'General Exams')
        product = Product.objects.filter(id=1639).first()
        examList = Event.objects.filter(Q(product= product) & Q(start_exam_date__gte=datetime.datetime.now())).order_by('start_date')
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







class GetCategoryProductList(APIView):
    pagination_class = CustomPagination
    serializer_class = ProductSerializer

    def get(self, request, *args,**kwargs):
        result = {
            "status": False,
            "msg": "Done"
        }
        category =productCategory.objects.filter(id=self.kwargs['id']).first()
        productList = Product.objects.filter(category=category ).order_by('name')
        # productList = Product.objects.filter(Q(category=category) & Q(start_date__gte=datetime.datetime.now())).order_by('start_date')

        page = self.paginate_queryset(productList)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            productSerializer = self.get_paginated_response(serializer.data)

        return Response(productSerializer.data, status=status.HTTP_200_OK)



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





class GetEventListByproductID(APIView):
    pagination_class = CustomPagination
    serializer_class = EventSerializer

    def get(self, request, *args,**kwargs):
        result = {
            "status": False,
            "msg": "Done"
        }
        print("Here")
        id = self.kwargs['id']
        product=Product.objects.filter(id=id).first()
        print(id)
        event_list =Event.objects.filter(Q(product=product) & Q(start_exam_date__gte=datetime.datetime.now())).filter(visible=True).order_by('start_date')
        # productList = Product.objects.filter(category=category)
        page = self.paginate_queryset(event_list)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            productSerializer = self.get_paginated_response(serializer.data)

        return Response(productSerializer.data, status=status.HTTP_200_OK)





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



