def gather_credits(credits_needed, *args):
    completed_courses = []
    total_credit = 0

    for course_name, credit in args:
        credit = int(credit)

        if course_name not in completed_courses:
            completed_courses.append(course_name)
            total_credit += credit

        if total_credit >= credits_needed:
            return f"Enrollment finished! Maximum credits: {total_credit}.\nCourses: {', '.join(course for course in sorted(completed_courses))}"

    return f"You need to enroll in more courses! You have to gather {credits_needed - total_credit} credits more."

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Advanced", 27),
    ("Advanced", 27),
))
