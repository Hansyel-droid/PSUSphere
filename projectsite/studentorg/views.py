from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, Member, Student, College, Program
from studentorg.forms import OrganizationForm, MemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

class HomePageView(ListView):
  model = Organization
  context_object_name = 'home'
  template_name = "home.html"

  def get_context_data(self, **kwargs):

    context = super().get_context_data(**kwargs)
    context["total_students"] = Student.objects.count()

    today = timezone.now().date()
    count = (
      Member.objects.filter(
        date_joined__year=today.year
      )
      .values("student")
      .distinct()
      .count()
    )

    context["students_joined_this_year"] = count
    return context

class OrganizationList(ListView):
  model = Organization
  context_object_name = 'organization'
  template_name = 'org_list.html'
  paginate_by = 5
  ordering = ["college__college_name","name"]

  def get_queryset(self):
    qs = super().get_queryset()
    query = self.request.GET.get('q')

    if query:
      qs = qs.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
      )
    return qs

class OrganizationCreateView(CreateView):
  model = Organization
  form_class = OrganizationForm
  template_name = 'org_form.html'
  success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
	model = Organization
	form_class = OrganizationForm
	template_name = 'org_form.html'
	success_url = reverse_lazy('organization-list')
    
class OrganizationDeleteView(DeleteView):
  model = Organization
  template_name = 'org_del.html'
  success_url = reverse_lazy('organization-list')

class MembersListView(ListView):
  model = Member
  context_object_name = 'member'
  template_name = 'member_list.html'
  paginate_by = 5

class MembersCreateView(CreateView):
  model = Member
  form_class = MemberForm
  template_name = 'member_form.html'
  success_url = reverse_lazy('member-list')

class MembersUpdateView(UpdateView):
  model = Member
  form_class = MemberForm
  template_name = 'member_form.html'
  success_url = reverse_lazy('member-list')

class MembersDeleteView(DeleteView):
  model = Member
  template_name = 'member_del.html'
  success_url = reverse_lazy('member-list')

class StudentListView(ListView):
  model = Student
  context_object_name = 'student'
  template_name = 'student_list.html'
  paginate_by = 5

class StudentCreateView(CreateView):
  model = Student
  form_class = StudentForm
  template_name = 'student_form.html'
  success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
  model = Student
  form_class = StudentForm
  template_name = 'student_form.html'
  success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
  model = Student
  template_name = 'student_del.html'
  success_url = reverse_lazy('student-list')

class CollegeListView(ListView):
  model = College
  context_object_name = 'college'
  template_name = 'college_list.html'
  paginate_by = 5

class CollegeCreateView(CreateView):
  model = College
  form_class = CollegeForm
  template_name = 'college_form.html'
  success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
  model = College
  form_class = CollegeForm
  template_name = 'college_form.html'
  success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
  model = College
  template_name = 'college_del.html'
  success_url = reverse_lazy('college-list')

class ProgramListView(ListView):
  model = Program
  context_object_name = 'program'
  template_name = 'program_list.html'
  paginate_by = 5
   
  def get_ordering(self):
    allowed = ["prog_name", "college__college_name"]
    sort_by = self.request.GET.get("sort_by")
    if sort_by in allowed:
      return sort_by
    return "prog_name"

class ProgramCreateView(CreateView):
  model = Program
  form_class = ProgramForm
  template_name = 'program_form.html'
  success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
  model = Program
  form_class = ProgramForm
  template_name = 'program_form.html'
  success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
  model = Program
  template_name = 'program_del.html'
  success_url = reverse_lazy('program-list')