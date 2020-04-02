from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

from .serializers import StatusSerializer
from ..models import Status
from status.api.serializers import StatusSerializer
from rest_framework.renderers import JSONRenderer

obj = Status.objects.first()
serializer1 = StatusSerializer(obj)
serializer1.data
json_data1 = JSONRenderer().render(serializer1.data)
print(json_data1)
stream1 = BytesIO(json_data1)
data1 = JSONParser().parse(stream1)
print(data1)

qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer1.data)
print(json_data2)
stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)

'''
Create Object
'''
data = {'user': 1}
serializer = StatusSerializer(data=data)
serializer.is_valid()
serializer.save()

'''
Update obj
'''
obj = Status.objects.first()
data = {'content': 'some new content', 'user': 1}
update_serializer = StatusSerializer(obj, data=data)
update_serializer.is_valid()
update_serializer.save()

'''
Delete obj
'''
data = {'user': 1, 'content': 'please delete me'}
create_obj_serializer = StatusSerializer(data=data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()  # instance of a the object
print(create_obj)

obj = Status.objects.last()
get_data_serializer = StatusSerializer(obj)
# update_serializer.is_valid()
# update_serializer.save()
print(obj.delete())

from rest_framework import serializers


class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()


data = {'email': 'hello@teamSanjeev.com', 'content': 'please delete me'}
create_obj_serializer = CustomSerializer(data=data)
if create_obj_serializer.is_valid():
    valid_data = create_obj_serializer.data
    print(valid_data)
