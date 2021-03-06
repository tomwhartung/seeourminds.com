""" views.py for our content app

Purpose: define the views for this app
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

import json
import textwrap

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import loader
from django.views.generic.base import View

from .adsense import adsense_ads
from .affiliate_marketing import AffiliateLinks
from .database import Questionnaire
from .forms import QuestionnaireForm
from .models import GalleriesList, Gallery, Image, Score


def home(request):

    """ Load and render the Home page template """

    template = loader.get_template('content/home.html')
    title = 'SeeOurMinds.com';
    context = {
        'adsense_ads': adsense_ads,
        'fixed_top': "fixed-top",
        'include_logo': False,
        'navbar_color': '',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def image(request, gallery_file_name=None, image_id=None):

    """ Render the single image template """

    this_image = Image(gallery_file_name, image_id)
    this_image.set_compare_contrast()
    image_dict = this_image.image_dict
    back_to_gallery_href = '/gallery/' + gallery_file_name + '/'

    afl_links = AffiliateLinks()
    afl_content = afl_links.afl_content
    afl_button = afl_links.afl_content

    title = image_dict.get('title')
    return render(request, 'content//galleries/gallery_image.html', {
        'adsense_ads': adsense_ads,
        'afl_content': afl_content,
        'afl_button': afl_button,
        'back_to_gallery_href': back_to_gallery_href,
        'image_dict': image_dict,
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    })


def index(request):

    """ Load and render the index page template """

    template = loader.get_template('content/index.html')
    title = 'index page'
    context = {
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def versions(request):

    """ Load and render the versions template """

    import platform
    python_version = platform.python_version()
    import django
    django_version_1 = django.VERSION
    django_version_2 = django.get_version()

    from .database import DJANGO_DEBUG
    from .database import RUNNING_LOCALLY

    template = loader.get_template('content/versions.html')
    title = 'versions page'
    context = {
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
        'django_version_1': django_version_1,
        'django_version_2': django_version_2,
        'python_version': python_version,
        'DJANGO_DEBUG': DJANGO_DEBUG,
        'RUNNING_LOCALLY': RUNNING_LOCALLY,
    }
    return HttpResponse(template.render(context, request))


##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Gallery Pages
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##

def galleries_list(request, galleries_list_name='all'):

    """
    Load and render the template displaying the list of Galleries
        appropriate for the passed-in galleries_list_name
    """

    galleries_list_obj = GalleriesList(galleries_list_name)
    galleries_list_obj.set_galleries_list_data()
    title = galleries_list_obj.galleries_list_title
    template = loader.get_template('content/galleries/galleries_list.html')
    context = {
        'galleries_list_obj': galleries_list_obj,
        'adsense_ads': adsense_ads,
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def gallery(request, gallery_file_name='None'):

    """ Load and render the template for a single Gallery page """

    if gallery_file_name == 'None':
        gallery_file_name = '0000-generic_images'

    this_gallery = Gallery(gallery_file_name)

    if len(this_gallery.gallery_dict) == 0:
        redirect_url = '/404/' + '/gallery/' + gallery_file_name
        return redirect(redirect_url, unknown_page=gallery_file_name)

    this_gallery.set_image_list_data()
    gallery_dict = this_gallery.gallery_dict
    title = gallery_dict.get('gallery_title')

    afl_links = AffiliateLinks()
    afl_content = afl_links.afl_content
    afl_button = afl_links.afl_content

    template = loader.get_template('content/galleries/galleries_gallery.html')
    context = {
        'gallery_dict': gallery_dict,
        'adsense_ads': adsense_ads,
        'afl_content': afl_content,
        'afl_button': afl_button,
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return HttpResponse(template.render(context, request))

##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Legal Pages
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##

def legal(request):

    """ Load and render the default legal template for this site """

    return redirect('/legal/terms_of_service')


def affiliate_marketing_disclosure(request):

    """ Load and render the affiliate_marketing_disclosure template """

    title = 'Disclosure - SeeOurMinds.com';
    template = 'content/legal/affiliate_marketing_disclosure.html'
    context = {
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return render(request, template, context)


def privacy_policy(request):

    """ Load and render the privacy_policy template """

    title = 'Privacy Policy - SeeOurMinds.com';
    template = 'content/legal/privacy_policy.html'
    context = {
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return render(request, template, context)


def questionnaire_disclaimer(request):

    """ Load and render the questionnaire_disclaimer template """

    title = 'Disclaimer - SeeOurMinds.com';
    template = 'content/legal/questionnaire_disclaimer.html'
    context = {
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return render(request, template, context)


def terms_of_service(request):

    """ Load and render the terms_of_service template """

    title = 'Terms of Service - SeeOurMinds.com';
    template = 'content/legal/terms_of_service.html'
    context = {
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'title': title,
    }
    return render(request, template, context)

##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Quiz Pages
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##

def quiz_about(request):

    """ Load and render the quiz_about page template """

    title = 'About the Quiz - SeeOurMinds.com';
    quiz_info = {}
    quiz_info["quiz_size_abbr"] = ''
    quiz_info["question_count"] = 0
    quiz_info["size_text"] = ''

    quiz_list_data = Questionnaire.get_quiz_list_data()
    template = loader.get_template('content/quiz/quiz_about.html')
    context = {
        'adsense_ads': adsense_ads,
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'quiz_info': quiz_info,
        'quiz_list_data': quiz_list_data,
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def quiz_form(request, quiz_size_slug=Questionnaire.DEFAULT_QUIZ_SIZE_SLUG):

    """ Load and render the quiz_form page template """

    quiz_menu_data = Questionnaire.get_quiz_menu_data()
    quiz_form = None
    if request.method == 'POST':
        # print('views.quiz_form() - request.POST:', request.POST)
        try:
            name = request.POST["name"]
        except:
            name = ''
        # print('views.quiz_form() - name:', name)
        #
        # BEGIN CRUFT ALERT!!
        #   2020-08-16: Disabling option to save results on server
        #   Therefore:
        #     this try...except statement and
        #     the if "Load"... clause
        #   are cruft:
        #   Real code resumes in the else clause
        #
        try:                                             # CRUFT ...
            email = request.POST["email"]
            load_answers = request.POST["load-answers"]
        except:                                          # ... CRUFT ...
            email = ''
            load_answers = ''
        if "Load" in load_answers:                       # ... CRUFT ...
            if email == '':
                need_email_msg = 'ERROR: you must enter a valid ' + \
                    'email address to load the answers'
                messages.add_message(request, messages.ERROR, need_email_msg)
            else:
                questionnaire = Questionnaire()
                new_request_data = questionnaire.add_answers(email, request)
                # print('views.quiz() - new_request_data:', new_request_data)
                quiz_form = QuestionnaireForm(
                        quiz_size_slug=quiz_size_slug, data=new_request_data)
        # ... END CRUFT ALERT!!
        else:  # Not loading answers, this is a questionnaire form submission
            quiz_form = QuestionnaireForm(
                    quiz_size_slug=quiz_size_slug, data=request.POST)
            if quiz_form.is_valid():
                # print('views.quiz() - quiz_form is_valid')
                score = Score()
                score.score_quiz(quiz_size_slug, quiz_form.cleaned_data)
                question_count = score.question_count
                if score.is_complete():
                    # print('views.quiz() - score is_complete')
                    title = 'Quiz Results - SeeOurMinds.com';
                    score.set_quiz_results_messages(request)
                    ###
                    ### 2020-08-16: Disabling option to save results on server
                    ### saved_messages = score.save_questionnaire(
                    ###         quiz_form.cleaned_data, quiz_size_slug)
                    ### for saved_msg in saved_messages:
                    ###     messages.add_message(request, messages.INFO, saved_msg)
                    template = loader.get_template('content/quiz/quiz_results.html')
                    score_for_context = score.as_list_of_pairs()
                    context = {
                        'score': score_for_context,
                        'question_count': question_count,
                        'fixed_top': "",
                        'include_logo': True,
                        'name': name,
                        'navbar_color': 'red darken-3',
                        'quiz_menu_data': quiz_menu_data,
                        'title': title,
                    }
                    return HttpResponse(template.render(context, request))
                else:
                    score.set_incomplete_message(request)

    if quiz_form == None:
        quiz_form = QuestionnaireForm(quiz_size_slug=quiz_size_slug)

    title = 'Quiz Form - SeeOurMinds.com';
    quiz_info = {}
    quiz_info["quiz_size_slug"] = quiz_size_slug
    quiz_info["quiz_size_abbr"] = \
        Questionnaire.get_quiz_size_abbr_for_slug(quiz_size_slug)
    quiz_info["question_count"] = \
        Questionnaire.get_question_count_for_slug(quiz_size_slug)
    quiz_info["size_text"] = \
        Questionnaire.get_quiz_size_text_for_slug(quiz_size_slug)

    template = loader.get_template('content/quiz/quiz_form.html')
    context = {
        'adsense_ads': adsense_ads,
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_form': quiz_form,
        'quiz_info': quiz_info,
        'quiz_menu_data': quiz_menu_data,
        'title': title,
    }
    return HttpResponse(template.render(context, request))

##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Pages for Google
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##

def google203aca4a4dd53796(request):

    """ Load and render the google203aca4a4dd53796 verification template """

    template = loader.get_template('content/google/google203aca4a4dd53796.html')
    context = {}
    return HttpResponse(template.render(context, request))


def google428ef5aab2bc0870(request):

    """ Load and render the google428ef5aab2bc0870 verification template """

    template = loader.get_template('content/google/google428ef5aab2bc0870.html')
    context = {}
    return HttpResponse(template.render(context, request))

##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views to suppoert shortcuts e.g., to a specific gallery and 404 not found
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##

def process_shortcut(request, unknown_page='default_unk_pg_1'):

    """ Process recognized shortcuts, and default to 404 """

    gallery_shortcuts = [
        'cheers',
        'deadwood',
        'game_of_thrones',
        'presidents',
        'star_wars',
        'the_wire',
        'true_detective',
        'twin_peaks'
    ]
    redirect_dict = {
        'cousins': '/gallery/7020-real-family-cousins/',
        'fam': '/gallery/7000-real-family-immediate/',
        'family': '/gallery/7000-real-family-immediate/',
        'ff': '/gallery/4900-real-politicians-founding_fathers/',
        'founding_fathers': '/gallery/4900-real-politicians-founding_fathers/',
        'sw': '/galleries/star_wars/',
        'star_wars': '/galleries/star_wars/',
        'anakin': '/image/1220-fictional-movies-star_wars-prequel/1222/',
        'han': '/image/1200-fictional-movies-star_wars-original/1206/',
        'leia': '/image/1200-fictional-movies-star_wars-original/1203/',
        'luke': '/image/1200-fictional-movies-star_wars-original/1200/',
        'padme': '/image/1220-fictional-movies-star_wars-prequel/1220/',
        'sheev': '/image/1220-fictional-movies-star_wars-prequel/1226/',
        'vader': '/image/1200-fictional-movies-star_wars-original/1209/',
        'got': '/galleries/game_of_thrones/',
        'jon': '/image/1410-fictional-tv-game_of_thrones-house_stark/1413/',
        'tywin': '/image/1430-fictional-tv-game_of_thrones-house_lannister/1431/',
        'sansa': '/image/1410-fictional-tv-game_of_thrones-house_stark/1415/',
        'arya': '/image/1410-fictional-tv-game_of_thrones-house_stark/1416/',
        'sopranos': '/gallery/2400-fictional-tv-sopranos/',
        'st': '/gallery/3900-fictional-tv-star_trek/',
        'star_trek': '/gallery/3900-fictional-tv-star_trek/',
        'tp': '/galleries/twin_peaks/',
        'wire': '/galleries/the_wire/',
        'xf': '/gallery/3700-fictional-tv-x_files/',
        'x-files': '/gallery/3700-fictional-tv-x_files/',
        'x_files': '/gallery/3700-fictional-tv-x_files/',
        'fox': '/image/3700-fictional-tv-x_files/3700/',
        'dana': '/image/3700-fictional-tv-x_files/3704/',
        'clinton': '/image/5040-real-politicians-us_presidents-1900s/5078/',
        'nixon': '/image/5040-real-politicians-us_presidents-1900s/5062/',
        'reagan': '/image/5040-real-politicians-us_presidents-1900s/5074/',
        'ah': '/image/4900-real-politicians-founding_fathers/4900/',
        'alexander_hamilton': '/image/4900-real-politicians-founding_fathers/4900/',
        'bf': '/image/4900-real-politicians-founding_fathers/4902/',
        'ben_franklin': '/image/4900-real-politicians-founding_fathers/4902/',
        'er': '/image/0500-real-famous-american-celebrities/0509/',
        'eleanor_roosevelt': '/image/0500-real-famous-american-celebrities/0509/',
        'fdr': '/image/5040-real-politicians-us_presidents-1900s/5048/',
        'franklin_roosevelt': '/image/5040-real-politicians-us_presidents-1900s/5048/',
        'gw': '/image/5000-real-politicians-us_presidents-1700s-1800s/5000/',
        'george_washington': '/image/5000-real-politicians-us_presidents-1700s-1800s/5000/',
        'jfk': '/image/5040-real-politicians-us_presidents-1900s/5058/',
        'john_kennedy': '/image/5040-real-politicians-us_presidents-1900s/5058/',
        'lbj': '/image/5040-real-politicians-us_presidents-1900s/5060/',
        'lyndon_johnson': '/image/5040-real-politicians-us_presidents-1900s/5060/',
        'ja': '/image/5000-real-politicians-us_presidents-1700s-1800s/5001/',
        'john_adams': '/image/5000-real-politicians-us_presidents-1700s-1800s/5001/',
        'mt': '/image/0500-real-famous-american-celebrities/0500/',
        'mark_twain': '/image/0500-real-famous-american-celebrities/0500/',
        'ph': '/image/4900-real-politicians-founding_fathers/4905/',
        'patrick_henry': '/image/4900-real-politicians-founding_fathers/4905/',
        'tj': '/image/5000-real-politicians-us_presidents-1700s-1800s/5003/',
        'thomas_jefferson': '/image/5000-real-politicians-us_presidents-1700s-1800s/5003/',
        'tr': '/image/5040-real-politicians-us_presidents-1900s/5040/',
        'theodore_roosevelt': '/image/5040-real-politicians-us_presidents-1900s/5040/',
        'ww': '/image/5040-real-politicians-us_presidents-1900s/5042/',
        'woodrow_wilson': '/image/5040-real-politicians-us_presidents-1900s/5042/',
        '2020-reps': '/gallery/5200-real-politicians-2020-incumbents/',
        '2020-incumbents': '/gallery/5200-real-politicians-2020-incumbents/',
        'donald': '/image/5200-real-politicians-2020-incumbents/5200/',
        'mike': '/image/5200-real-politicians-2020-incumbents/5202/',
        'steveb': '/image/0500-real-famous-american-celebrities/0517/',
        'nancy': '/image/5200-real-politicians-2020-incumbents/5208/',
        'mitch': '/image/5200-real-politicians-2020-incumbents/5206/',
        '2020-dems': '/gallery/5210-real-politicians-2020-democratic-candidates/',
        'joe': '/image/5210-real-politicians-2020-democratic-candidates/5215/',
        'kamala': '/image/5210-real-politicians-2020-democratic-candidates/5216/',
        '2019-candidates': '/gallery/5390-real-politicians-presidential_contenders-2019/',
        'bernie': '/image/5390-real-politicians-presidential_contenders-2019/5391/',
        'cory': '/image/5390-real-politicians-presidential_contenders-2019/5392/',
        'elizabeth': '/image/5390-real-politicians-presidential_contenders-2019/5393/',
        'nikki': '/image/5300-real-politicians-authors/5304/',
        'don_jr': '/image/5300-real-politicians-authors/5300/',
    }

    unk_pg_lc = unknown_page.lower()

    if unk_pg_lc in gallery_shortcuts:
        redirect_url = '/galleries/' + unk_pg_lc +'/'
    elif unk_pg_lc in redirect_dict.keys():
        redirect_url = redirect_dict[unk_pg_lc]
    else:
        redirect_url = '/404/' + unk_pg_lc

    return redirect(redirect_url, unknown_page=unk_pg_lc)


def not_found(request, unknown_page='default_unk_pg_2'):

    """ Load and render the 404 not found template """

    template = loader.get_template('content/404.html')
    context = {
        'fixed_top': "",
        'include_logo': True,
        'navbar_color': 'red darken-3',
        'quiz_menu_data': Questionnaire.get_quiz_menu_data(),
        'unknown_page': unknown_page,
    }
    return HttpResponse(template.render(context, request))
