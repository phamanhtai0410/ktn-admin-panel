from datetime import date, datetime
from dateutil import tz
from flask_admin.model import typefmt
import json
from flask_admin._compat import text_type


def date_format(view, value):
    time_zone = tz.gettz('Asia/Ho_Chi_Minh')
    value = value.astimezone(time_zone)
    return value.strftime('%d-%m-%Y %H:%M:%S')



DEFAULT_TYPE_FORMATTER = dict(typefmt.BASE_FORMATTERS)
DEFAULT_TYPE_FORMATTER.update({
        type(None): typefmt.null_formatter,
        date: date_format,
    })