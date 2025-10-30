# work10/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Todo
from .forms import TodoForm, SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

class TodoListView(LoginRequiredMixin, generic.ListView):
    model = Todo
    template_name = 'work10/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        # ログインユーザーのTODOのみを表示
        return Todo.objects.filter(created_by=self.request.user).order_by('-created_at')

class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'work10/todo_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'work10/todo_form.html'

    def test_func(self):
        todo = self.get_object()
        return todo.created_by == self.request.user

class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Todo
    template_name = 'work10/todo_confirm_delete.html'
    success_url = reverse_lazy('work10:todo_list')

    def test_func(self):
        todo = self.get_object()
        return todo.created_by == self.request.user

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('work10:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())
