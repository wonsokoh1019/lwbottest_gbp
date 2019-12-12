#!/bin/env python
# -*- coding: utf-8 -*-
"""
Handle the user's manual check-out
"""

__all__ = ['manual_sign_out_message', 'manual_sign_out_content', 'manual_sign_out']

import tornado.web
import asyncio
import logging
from attendance_management_bot.model.i18n_data import make_i18n_text
from attendance_management_bot.externals.send_message import push_messages
from attendance_management_bot.actions.message import invalid_message, \
    prompt_input
from attendance_management_bot.model.processStatusDBHandle \
    import get_status_by_user, set_status_by_user_date
import gettext
_ = gettext.gettext

LOGGER = logging.getLogger("attendance_management_bot")


def manual_sign_out_message():
    """
    generate manual check-out message

    :return: message content list
    """
    fmt = _("Please manually enter the clock-out time.")
    text1 = make_i18n_text("Please manually enter the clock-out time.",
                      "manual_sign_out", fmt)

    text2 = prompt_input()

    return [text1, text2]


@tornado.gen.coroutine
def manual_sign_out_content(account_id, current_date):
    """
    Update user status and generate manual check-out message.

    :param account_id: user account id
    :param current_date: current date by local time.
    :return: message content list
    """

    content = get_status_by_user(account_id, current_date)
    process = None
    if content is not None:
        status = content[0]
        process = content[1]

    if process is None or process != "sign_in_done":
        return [invalid_message()]

    if status == "wait_out" or status == "out_done":
        set_status_by_user_date(account_id, current_date, status="in_done")

    yield asyncio.sleep(1)
    set_status_by_user_date(account_id, current_date, "wait_out")

    return manual_sign_out_message()


@tornado.gen.coroutine
def manual_sign_out(account_id, current_date, _, __):
    """
    Handle the user's manual check-out.

    :param account_id: user account id.
    :param current_date: current date by local time.
    :param _: no use
    :param __: no use
    """
    contents = yield manual_sign_out_content(account_id, current_date)

    yield push_messages(account_id, contents)
