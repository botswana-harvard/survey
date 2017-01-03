# coding=utf-8

import sys

from dateutil.relativedelta import relativedelta

from edc_base.utils import get_utcnow

from .site_surveys import site_surveys
from .survey import Survey
from .survey_schedule import SurveySchedule


survey_one = SurveySchedule(
    name='year-1',
    group_name='test_survey',
    start_date=(get_utcnow() - relativedelta(years=3)).date(),
    end_date=(get_utcnow() - relativedelta(years=2)).date())

survey_two = SurveySchedule(
    name='year-2',
    group_name='test_survey',
    start_date=(get_utcnow() - relativedelta(years=2)).date(),
    end_date=(get_utcnow() - relativedelta(years=1)).date())

survey_three = SurveySchedule(
    name='year-3',
    group_name='test_survey',
    start_date=(get_utcnow() - relativedelta(years=1)).date(),
    end_date=get_utcnow().date())

baseline = Survey(
    name='baseline',
    position=0,
    map_area='test_community',
    start_date=(get_utcnow() - relativedelta(years=3)).date(),
    end_date=(get_utcnow() - relativedelta(years=2)).date(),
    full_enrollment_date=(get_utcnow() - relativedelta(years=2)).date()
)

annual_1 = Survey(
    name='annual-1',
    position=1,
    map_area='test_community',
    start_date=(get_utcnow() - relativedelta(years=3)).date(),
    end_date=(get_utcnow() - relativedelta(years=2)).date(),
    full_enrollment_date=(get_utcnow() - relativedelta(years=2)).date()
)

annual_2 = Survey(
    name='annual-2',
    position=2,
    map_area='test_community',
    start_date=(get_utcnow() - relativedelta(years=3)).date(),
    end_date=(get_utcnow() - relativedelta(years=2)).date(),
    full_enrollment_date=(get_utcnow() - relativedelta(years=2)).date()
)

survey_one.add_survey(baseline, annual_1, annual_2)

# SurveySchedule(name='bcpp-year-2')
# SurveySchedule(name='bcpp-year-3')

if 'test' in sys.argv:
    site_surveys.register(survey_one)
    site_surveys.register(survey_two)
    site_surveys.register(survey_three)