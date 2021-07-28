from rest_framework import serializers
from news_scrape.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        # To simplify the uniqueness logic, make item id read_only
        read_only_fields = ['item_id', 'deleted',
                            'dead', 'kids', 'descendants',
                            'is_posted']
