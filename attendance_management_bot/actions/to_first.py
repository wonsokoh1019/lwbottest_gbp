# !/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import logging
from attendance_management_bot.model.i18n_data import make_i18n_text
from attendance_management_bot.externals.send_message import push_message
import gettext
_ = gettext.gettext

LOGGER = logging.getLogger("attendance_management_bot")


@tornado.gen.coroutine
def to_first(account_id, ____, __, ___):
    fmt = _("Please select \"Record\" on the bottom of "
            "the menu each time when you clock in and clock out.")
    content = make_i18n_text("Please select \"Record\" on the bottom of the "
                             "menu each time when you clock in and clock out.",
                             "to_first", fmt)
    yield push_message(account_id, content)
