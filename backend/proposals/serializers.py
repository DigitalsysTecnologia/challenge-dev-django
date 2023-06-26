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
        last_proposal = Proposal.objects.all().last()

        if last_proposal:

            if last_proposal.accepted:
                attrs['accepted'] = False
            else:
                attrs['accepted'] = True

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
