
def gather_credits(credits_needed, *args):
    courses_enrolled = {}

    for course_name, credit in args:
        credit = int(credit)

        if course_name not in courses_enrolled.keys():
            courses_enrolled[course_name] = credit

        if sum(courses_enrolled.values()) >= credits_needed:
            return (f"Enrollment finished! Maximum credits: {sum(courses_enrolled.values())}.\n"
                    f"Courses: {', '.join(course for course in sorted(courses_enrolled))}")

    return (f"You need to enroll in more courses! "
            f"You have to gather {credits_needed - sum(courses_enrolled.values())} credits more.")