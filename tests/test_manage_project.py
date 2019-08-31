import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from model.project import Project
import pytest
import re
import random
from data.projects import testdata


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    old_projects = app.project.get_project_list()
    app.project.create(project)
    assert len(old_projects) + 1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create(Project(projectname="test_project", status="development", viewstatus="public",  description="test_description"))
    old_projects = app.project.get_project_list()
    project_to_delete = random.choice(old_projects)
    app.project.delete(project_to_delete)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.project.get_project_list()
    new_projects.append(project_to_delete)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

