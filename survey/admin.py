# coding=utf-8

from django.contrib import admin

from edc_base.modeladmin_mixins import ModelAdminBasicMixin

from .models import Survey
from .admin_site import survey_admin


@admin.register(Survey, site=survey_admin)
class SurveyAdmin (ModelAdminBasicMixin, admin.ModelAdmin):

    list_display = ('survey_name', 'survey_slug', 'chronological_order',
                    'datetime_start', 'datetime_end')
