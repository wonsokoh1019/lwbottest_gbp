********
DOCUMENT
********

heroku는 배포 후 Procfile 파일에서 정의된 작업을 자동으로 수행한다. 근태관리 봇의 Procfile은 환경을 초기화하고 `main.py` 를 수행해서 데몬을 실행한다.

그 외 근태관리 봇에서 API를 사용하는 함수를 소개한다.

    예시
    - `attendance_management_bot.externals.calendar_req.create_calendar` 의 실제 소스코드는 `attendance_management_bot/externals/calendar_req.py` 의 `create_calendar` 함수에서 확인할 수 있다.

개발 언어 및 환경
=================

- Python3
- Tornado framework
- Postgres

Procfile
========

https://devcenter.heroku.com/articles/procfile:

    Heroku apps include a Procfile that specifies the commands that are executed by the app on startup. You can use a Procfile to declare a variety of process types, including:
    - Your app’s web server
    - Multiple types of worker processes
    - A singleton process, such as a clock
    - Tasks to run before a new release is deployed

This bot's Procfile:

.. literalinclude:: ../Procfile
    :caption: Procfile



Initialize environment
======================

.. literalinclude:: ../scripts/initialize.py
    :caption: scripts/initialize.py

Initialize database
-------------------

.. autofunction:: attendance_management_bot.initDB.init_db
    :noindex:

.. autofunction:: attendance_management_bot.initDB.create_calendar_table
    :noindex:

.. autofunction:: attendance_management_bot.initDB.create_init_status_table
    :noindex:

.. autofunction:: attendance_management_bot.initDB.create_process_status_table
    :noindex:

Register bot
------------

.. autofunction:: attendance_management_bot.registerBot.init_bot
    :noindex:

.. autofunction:: attendance_management_bot.registerBot.register_bot
    :noindex:

.. autofunction:: attendance_management_bot.registerBot.register_bot_domain
    :noindex:

Run bot
=======

.. literalinclude:: ../main.py
    :caption: main.py

.. autofunction:: attendance_management_bot.attendance_management_bot.start_attendance_management_bot
    :noindex:

.. autofunction:: attendance_management_bot.router.getRouter
    :noindex:

.. autoclass:: attendance_management_bot.callbackHandler.CallbackHandler
    :members:
    :noindex:

.. autoclass:: attendance_management_bot.check_and_handle_actions.CheckAndHandleActions
    :members:
    :noindex:

Bot API functions
=================

.. autofunction:: attendance_management_bot.model.data.make_text
    :noindex:

.. autofunction:: attendance_management_bot.model.data.make_quick_reply
    :noindex:

.. autofunction:: attendance_management_bot.model.data.make_image_carousel
    :noindex:

.. autofunction:: attendance_management_bot.externals.send_message.push_message
    :noindex:

Calender API functions
======================

.. autofunction:: attendance_management_bot.externals.calendar_req.create_calendar
    :noindex:

.. autofunction:: attendance_management_bot.externals.calendar_req.create_schedule
    :noindex:

.. autofunction:: attendance_management_bot.externals.calendar_req.modify_schedule
    :noindex:

Bot rich menu functions
=======================

.. autofunction:: attendance_management_bot.externals.richmenu.upload_content
    :noindex:

.. autofunction:: attendance_management_bot.externals.richmenu.make_add_rich_menu_body
    :noindex:

.. autofunction:: attendance_management_bot.externals.richmenu.set_rich_menu_image
    :noindex:

.. autofunction:: attendance_management_bot.externals.richmenu.set_user_specific_rich_menu
    :noindex:

.. autofunction:: attendance_management_bot.externals.richmenu.get_rich_menus
    :noindex:

.. autofunction:: attendance_management_bot.externals.richmenu.cancel_user_specific_rich_menu
    :noindex:

Bot i18n functions
===================

https://docs.python.org/2/library/gettext.html

    You can use the. /tools/gen.sh tool to generate '. Po', '. Mo' files.
        execute:
            $: ./tools/gen.sh [filename] [po|mo] [path]
            "filename": Python source filename used to generate '.po','.mo'.
            "po|mo": 'po' means generate '.po' file, 'mo' means generate '.mo' file
            "path": Relative directory of Python source files. not ending with '/'.
            You can find the corresponding '.po' file in 'locales/../LC_MESSAGES' according to your source file name.
        step:
            1. generate '.po' file.
                eg:
                    ./tools/gen.sh test_i18n.py po test
                check: locales/../LC_MESSAGES/test_i18n.po
            2. Multilingual string to fill in '.po' file.
            3. generate '.mo' file
                eg:
                    ./tools/gen.sh test_i18n.py mo test
                check: locales/../LC_MESSAGES/test_i18n.mo

.. autofunction:: test.test_i18n.test_ko
    :noindex:

.. autofunction:: test.test_i18n.get_data
    :noindex:

.. autofunction:: attendance_management_bot.model.i18n_data.get_i18n_content_by_lang
    :noindex:

.. autofunction:: attendance_management_bot.model.i18n_data.get_i18n_content
    :noindex:

.. autofunction:: attendance_management_bot.model.i18n_data.make_i18n_button
    :noindex:

.. autofunction:: attendance_management_bot.model.i18n_data.make_i18n_text
    :noindex:

.. autofunction:: attendance_management_bot.model.i18n_data.make_i18n_message_action
    :noindex:

.. autofunction:: attendance_management_bot.model.i18n_data.make_il8n_image_carousel_column
    :noindex:

타임존 설정
===========

근태관리 봇의 타임존은 Asia/Tokyo로 설정되어있다. 변경을 원할 경우 소스 코드에서 원하는 국가/도시의 시간대로 변경 할 수 있다.

타임존 설정 소스 코드 위치
--------------------------

타임존을 설정 할 수 있는 소스 코드는 conf 폴더 내에 config.py 파일에서 #Timezone 항목에 위치한다.

타임존 변경 방법
----------------

TZone ="{원하는 국가/도시}" 로 변경할 수 있다.

    참고
    - 국가/도시명에 삽입되는 TZ database name은 해당 url에서 확인 할 수 있다 : https://developers.worksmobile.com/kr/document/1009006/v2?lang=ko

Indices and tables
==================

.. toctree::
    :maxdepth: 4

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
