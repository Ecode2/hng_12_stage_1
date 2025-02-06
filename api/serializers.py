from rest_framework import serializers


class NumberClassifySerializer(serializers.Serializer):
    number = serializers.IntegerField()
    is_prime = serializers.BooleanField()
    is_perfect = serializers.BooleanField()
    properties = serializers.ListField(child=serializers.CharField(allow_blank=True), required=False)
    digit_sum = serializers.IntegerField()
    fun_fact = serializers.CharField()
