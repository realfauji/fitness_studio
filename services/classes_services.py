from utils.file_ops import read_json, write_json
from utils.timezone import convert_timezone


CLASSES_FILE = "data/classes.json"

def get_all_classes(timezone: str = None):
    classes = read_json(CLASSES_FILE)
    if timezone:
        for cls in classes:
            cls["datetime"] = convert_timezone(cls["datetime"], timezone).isoformat()
    return classes

def reduce_slot(class_id: int) -> bool:
    classes = read_json(CLASSES_FILE)
    for cls in classes:
        if cls["id"] == class_id and cls["slots"] > 0:
            cls["slots"] -= 1
            write_json(CLASSES_FILE, classes)
            return True
    return False
