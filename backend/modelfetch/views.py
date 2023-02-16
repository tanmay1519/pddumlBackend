from matplotlib import test
from rest_framework.views import APIView
# from .models import *
from rest_framework.response import Response

import pickle
class GetTomato (APIView):
    def post (self,request) :
        output = {}
        img_data  = request.data['tomato_unhealthy']
        print(type(img_data))
        pickled_model = pickle.load(open('model.pkl', 'rb'))
        output["result"] = pickled_model.predict([img_data])
        output['status']="Success"
        print(output,"TANMAY")
        return Response(output)

