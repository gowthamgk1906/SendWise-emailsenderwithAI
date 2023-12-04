# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

class AIChatView(APIView):
    def post(self, request, *args, **kwargs):
        chatbot_response = None
        if api_key is not None and request.method =='POST':
            openai.api_key = api_key
            user_input = request.data.get('user_input')
            prompt = user_input

            response = openai.completions.create(
                model='text-davinci-003',
                prompt=prompt,
                max_tokens=256,
                temperature=0.5
            )
            chatbot_response = response.choices[0].text

        return Response({'chatbot_response': chatbot_response}, status=status.HTTP_200_OK)
