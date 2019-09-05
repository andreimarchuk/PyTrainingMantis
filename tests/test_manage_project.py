import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from model.project import Project
import pytest
import string
import random
from data.projects import testdata


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_progect_list(username, password)
    app.project.create(project)
    assert len(old_projects) + 1 == app.project.count()
    new_projects = app.soap.get_progect_list(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create(Project(projectname="test_project", status="development", viewstatus="public",  description="test_description"))
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_progect_list(username, password)
    project_to_delete = random.choice(old_projects)
    app.project.delete(project_to_delete)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.soap.get_progect_list(username, password)
    new_projects.append(project_to_delete)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

