from django.db.models import Sum
from django.shortcuts import render
from .models import Topic, New


# Create your views here.
def dashboard(request):
    return render(request, 'topics/dashboard.html')


def topics(request):
    topics_all = Topic.objects.all()
    topic_name_count_valueSum_list = []

    for topic in topics_all:
        topic_count = topic.new_set.count()
        topic_value_sum_dict = topic.new_set.aggregate(Sum('value'))
        topic_value_sum = topic_value_sum_dict['value__sum']

        topic_name_count_valueSum = {}
        topic_name_count_valueSum.update({'topic': topic})
        topic_name_count_valueSum.update({'topicName': str(topic)})
        topic_name_count_valueSum.update({'count': topic_count})
        topic_name_count_valueSum.update({'valueSum': topic_value_sum})
        topic_name_count_valueSum_list.append(topic_name_count_valueSum)

    context = {'topicNameCountValueSum': topic_name_count_valueSum_list}
    return render(request, 'topics/dashboard.html', context)


def topic_detail(request, pk_test):
    topic = Topic.objects.get(id=pk_test)
    topic_news_order_latest = topic.new_set.all().order_by('-date_created')
    topic_news_order_value = topic.new_set.all().order_by('-value')

    context = {'topic': topic, 'topic_news_order_latest': topic_news_order_latest,
               'topic_news_order_value': topic_news_order_value}
    return render(request, 'topics/topic.html', context)


def news(request):
    news_all = New.objects.all().order_by('-date_created')
    context = {"news": news_all}
    return render(request, 'topics/news-list.html', context)
