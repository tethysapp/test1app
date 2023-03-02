from tethys_sdk.base import TethysAppBase


class Test1App(TethysAppBase):
    """
    Tethys app class for Test1App.
    """

    name = 'Test1App'
    description = ''
    package = 'test1app'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'test1app'
    color = '#718093'
    tags = ''
    enable_feedback = False
    feedback_emails = []