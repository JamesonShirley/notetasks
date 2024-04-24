from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.utils.safestring import mark_safe
from django.utils.dateformat import format
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Note, Task
from .forms import TaskForm
from django.shortcuts import render
from django.utils.dateparse import parse_date
from django.db.models import Q


# Note Views
class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/note_list.html'

    def get_queryset(self):
        queryset = Note.objects.order_by('-created_at')

        search_query = self.request.GET.get('search', '')
        date_created_str = self.request.GET.get('date_created', '')

        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

        if date_created_str:
            if 'to' in date_created_str:
                start_date_str, end_date_str = date_created_str.split(' to ')
                start_date = parse_date(start_date_str.strip())
                end_date = parse_date(end_date_str.strip())
                queryset = queryset.filter(created_at__date__gte=start_date, created_at__date__lte=end_date)
            else:
                created_date = parse_date(date_created_str.strip())
                if created_date:
                    queryset = queryset.filter(created_at__date=created_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['date_created'] = self.request.GET.get('date_created', '')
        return context


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note_detail.html'


class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')


class NoteDeleteView(DeleteView):
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('note_list')
    template_name = 'notes/note_confirm_delete.html'


# Task Views
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        queryset = Task.objects.order_by('-deadline')

        due_date_str = self.request.GET.get('due_date')
        completed_str = self.request.GET.get('completed')
        search_query = self.request.GET.get('search')

        if due_date_str:
            due_date = parse_date(due_date_str)
            if due_date:
                queryset = queryset.filter(deadline__date=due_date)

        if completed_str:
            completed = completed_str.lower() == 'true'
            queryset = queryset.filter(completed=completed)

        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        completed_task_count = context['tasks'].filter(completed=True).count()
        progress_percentage = (completed_task_count / 10) * 100

        context['completed_task_count'] = completed_task_count
        context['progress_percentage'] = progress_percentage
        context['due_date'] = self.request.GET.get('due_date', '')
        context['completed'] = self.request.GET.get('completed', '')
        context['search_query'] = self.request.GET.get('search', '')

        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
    template_name = 'tasks/task_confirm_delete.html'


class CalendarView(TemplateView):
    template_name = 'tasks/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()

        task_events = [
            {
                'title': str(task.title),
                'start': format(task.deadline, 'c'),
                'end': format(task.deadline, 'c'),
                'url': reverse_lazy('task_edit', args=[task.id]),
            } for task in tasks
        ]

        context['task_events_json'] = mark_safe(json.dumps(task_events, cls=DjangoJSONEncoder))
        return context
