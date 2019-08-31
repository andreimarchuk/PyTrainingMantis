from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(3, maxlen))])


testdata = [Project(projectname=random_string("Project_", 10), status="development",
                    viewstatus="public", description=random_string("description_", 20))
    for i in range(5)
]

