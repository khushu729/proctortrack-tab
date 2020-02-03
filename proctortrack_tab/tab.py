from django.utils.translation import ugettext_noop
from courseware.tabs import EnrolledTab


class ProctorTrackTab(EnrolledTab):
    """
    ProctortrackTab class will add new tab named "Proctor" in course details page.
    """
    name = "proctortrack_tab"
    title = ugettext_noop("Proctor")
    view_name = "proctortrack_view"
    tab_id = "proctortrack_tab"
    type = 'proctortrack_tab'
    is_default = True
    is_dynamic = True
    priority = 60

    @classmethod
    def is_enabled(cls, course, user=None):        
        return True
