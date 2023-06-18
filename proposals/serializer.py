import pdb

import cpf_generator
from cpf_generator import CPF
from rest_framework import serializers

from proposals.models import CustomUser, Proposal


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'cpf', 'address']


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['value', 'accepted', 'user']

    user = CustomUserSerializer()

    def validate(self, attrs):
        cpf = CPF.validate(attrs.get('user').get('cpf'))
        return super().validate(attrs)

    def save(self, **kwargs):
        return super().save(**kwargs)

    def create(self, validated_data):
        user = CustomUser.objects.filter(name=validated_data.get('user').get('name')).first()
        if not user:
            user = CustomUser.objects.create(
                name=validated_data.get('user').get('name'),
                cpf=validated_data.get('user').get('cpf'),
                address=validated_data.get('user').get('address')
            )
        validated_data['user'] = user
        instance = Proposal.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
