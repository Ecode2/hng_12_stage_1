import requests 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import NumberClassifySerializer

# Create your views here.
class NumberClassifierView(APIView):

    def get(self, request):
        try:
            query = request.query_params

            number_query = query["number"]
            number =int(number_query)

        except Exception as e:
            if type(e) == TypeError:
                error = {"number": number_query, "error": True}
            else:
                error = {"message":"query parameter must be number", "error": True}

            return  Response(error, status=status.HTTP_400_BAD_REQUEST)

        # get a fact about the number
        response = requests.get(f"http://numbersapi.com/{number}/math")
        if not response.ok:
            return  Response(status=status.HTTP_400_BAD_REQUEST)
        
        fact = response.text
        
        perfect = False
        if number % 2 == 0:
            perfect = True
        
        
        serializer = NumberClassifySerializer(data= {"number": number,
                                            "is_prime": self.is_prime(number),
                                            "is_perfect": perfect,
                                            "properties": self.get_properties(number),
                                            "digit_sum": self.get_digit_sum(number),
                                            "fun_fact": fact})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get_properties(self, number: int) -> list:
        properties = []

        # If the number is negative, only check if it's even or odd
        if number < 0:
            return ["even"] if number % 2 == 0 else ["odd"]

        # Check if the number is an Armstrong number
        digits = [int(d) for d in str(number)]
        power = len(digits)
        is_armstrong = sum(d ** power for d in digits) == number

        if is_armstrong:
            properties.append("armstrong")

        # Check if the number is even or odd
        properties.append("even" if number % 2 == 0 else "odd")

        return properties



    def is_prime(self, number: int) -> bool:
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    

    def get_digit_sum(self, number: int) -> int:
        # Use the absolute value of the number to avoid the '-' character
        return sum(int(d) for d in str(abs(number)))

    
