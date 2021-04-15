from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry
from django.db.models import Q


class HomeView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'entries/base.html'
    context_object_name = 'blog_entries'
    ordering = ['-entry_date']
    paginate_by = 5


class EntryView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'


class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['entry_title', 'entry_text']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)


class SearchResultsView(ListView):
    model = Entry
    template_name = 'entries/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Entry.objects.filter(
            Q(entry_title__icontains=query) | Q(entry_text__icontains=query)
        )
        return object_list
