# -*- coding: utf-8 -*-

__license__ = 'GPL 3'
__copyright__ = '2010, Li Fanxi <lifanxi@freemindworld.com>'
__docformat__ = 'restructuredtext en'

from calibre.gui2.convert.snb_output_ui import Ui_Form
from calibre.gui2.convert import Widget

newline_model = None


class PluginWidget(Widget, Ui_Form):

    TITLE = _('SNB Output')
    HELP = _('Options specific to')+' SNB '+_('output')
    COMMIT_NAME = 'snb_output'
    ICON = I('mimetypes/snb.png')

    def __init__(self, parent, get_option, get_help, db=None, book_id=None):
        Widget.__init__(self, parent,
                        ['snb_insert_empty_line', 'snb_dont_indent_first_line',
                            'snb_hide_chapter_name','snb_full_screen'])
        self.db, self.book_id = db, book_id
        self.initialize_options(get_option, get_help, db, book_id)


