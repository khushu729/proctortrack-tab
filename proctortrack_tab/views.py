import os

from edxmako.shortcuts import render_to_response
from edxmako.paths import add_lookup
from opaque_keys.edx.keys import CourseKey

from courseware.courses import get_course_with_access


def proctortrack_view(request, course_id):
    """
    View for Proctor tab. This will render page with iframe and 
    https://www.proctortrack.com/ url as iframe src attribute.
    """
    course_key = CourseKey.from_string(course_id)
    course = get_course_with_access(request.user, "load", course_key)
    add_lookup('main', os.path.join(os.path.dirname(os.path.dirname(__file__)), 'proctortrack_tab/templates'))
    iframe_src = 'https://www.proctortrack.com/'

    context = {
        "course": course,
        "iframe_src": iframe_src,
    }
    return render_to_response("proctortrack_tab/proctortrack_tab.html", context)
