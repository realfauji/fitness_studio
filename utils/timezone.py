from datetime import datetime
import pytz


def convert_timezone(dt_str: str, to_tz: str):
    ist = pytz.timezone("Asia/Kolkata")
    user_tz = pytz.timezone(to_tz)

    ist_time = ist.localize(datetime.fromisoformat(dt_str))
    return ist_time.astimezone(user_tz)
