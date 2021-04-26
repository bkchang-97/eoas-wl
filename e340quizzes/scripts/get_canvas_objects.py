"""
* get_canvas_students.py

example:
    python get_canvas_students.py  live/test a301/e340
"""
import argparse
import pdb
import pprint
import warnings

import context
import pandas as pd

from .utils import login_courses
from .utils import start_logging


def get_students(canvas_instance, course_name, ta_list=None):
    if ta_list is None:
        ta_list = ["NA"]
    canvas, keep = login_courses(canvas_instance)
    course = canvas.get_course(keep[course_name])
    all_students = course.get_enrollments()
    try:
        name_id_canid = [
            (
                item.user["sortable_name"],
                int(item.user["sis_user_id"]),
                int(item.user["id"]),
            )
            for item in all_students
            if (
                (item.user["sis_user_id"] is not None)
                and (item.user["sis_user_id"] not in ta_list)
            )
        ]
    except AttributeError:
        raise AttributeError("no students in course")
    df = pd.DataFrame.from_records(name_id_canid, columns=["name", "ubcid", "canvasid"])
    df["sort_order"] = list(range(len(df)))
    # pdb.set_trace()
    return course, df


def get_pages(course):
    all_pages = list(course.get_pages())
    return all_pages


def get_course(canvas_instance, course_name):
    canvas, keep = login_courses(canvas_instance)
    course = canvas.get_course(keep[course_name])
    return course


def get_page(course, pagid):
    the_page = course.get_page(pagid)
    return the_page


def get_modules(canvas_instance, course_name):
    # canvas, keep = login_courses(canvas_instance)
    canvas, keep = login_courses(canvas_instance)
    print(f"here is keep -- {pprint.pformat(keep)}")
    course = canvas.get_course(keep[course_name])
    all_students = course.get_enrollments()
    try:
        name_id_canid = [
            (item.user["sortable_name"], item.user["sis_user_id"], item.user["id"])
            for item in all_students
        ]
    except AttributeError:
        raise AttributeError("no students in course")
    df = pd.DataFrame.from_records(name_id_canid, columns=["name", "id", "canid"])
    return course, df


def get_quizzes(canvas_instance, course_name):
    # canvas, keep = login_courses(canvas_instance)
    canvas, keep = login_courses(canvas_instance)
    print(f"here is keep -- {pprint.pformat(keep)}")
    course = canvas.get_course(keep[course_name])
    all_students = course.get_enrollments()
    try:
        name_id_canid = [
            (item.user["sortable_name"], item.user["sis_user_id"], item.user["id"])
            for item in all_students
        ]
    except AttributeError:
        raise AttributeError("no students in course")
    df = pd.DataFrame.from_records(name_id_canid, columns=["name", "id", "canid"])
    return course, df


def make_parser():
    """
    set up the command line arguments needed to call the program
    """
    linebreaks = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(
        formatter_class=linebreaks, description=__doc__.lstrip()
    )
    parser.add_argument("canvas_instance", type=str, help="either test or live")
    parser.add_argument("course", type=str, help="e340 or a301")
    return parser


def main(args=None, ta_list=None):
    parser = make_parser()
    args = parser.parse_args(args)
    course, df = get_students(args.canvas_instance, args.course)
    return course, df
    # assignments=course.get_assignments()
    # good_list=[item for item in assignments if item.published]
    # assign_names=[(item.name,item.attributes['id'],
    #                item.attributes['due_at']) for item in good_list]
    # submits=good_list[20].get_submissions()
    # all_submits=[item for item in submits]
    # out = good_list[20].get_submission(user=11732,include=['submission_history'])
    # print(out.__dict__['submission_history'][0]['submission_data'])
    # pdb.set_trace()


if __name__ == "__main__":
    main()
