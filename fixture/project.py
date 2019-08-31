import os
import random
import time
import re

from model.project import Project
import re


class ProjectHelper:

    def __init__(self, app):
        self.app = app



    def create(self, project):
        wd = self.app.wd
        self.app.return_to_manage_projects()
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        # fill contact form
        self.fill_project(project)
        # submit contact creation
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def delete(self, project):
        wd = self.app.wd
        self.app.return_to_manage_projects()
        wd.find_element_by_xpath("//a[contains (text(), '" + project.projectname + "')]").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        # confirmation
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def get_project_list(self):
        wd = self.app.wd
        self.app.return_to_manage_projects()
        l = []
        for element in wd.find_elements_by_xpath("//table[@class = 'width100']//tr[position()>2]"):
            id = re.match('.*?([0-9]+)$', element.find_element_by_xpath("td[1]//a").get_attribute("href")).group(1)
            projectname = element.find_element_by_xpath("td[1]").text
            status = element.find_element_by_xpath("td[2]").text
            viewstatus = element.find_element_by_xpath("td[4]").text
            description = element.find_element_by_xpath("td[5]").text
            l.append(Project(id=id, projectname=projectname, status=status, viewstatus=viewstatus, description=description))
        return list(l)

    def fill_project(self, project):
        self.app.change_value_by_name("name", project.projectname)
        self.app.select_element_in_dropdown("//select[@name='status']", project.status)
        self.app.select_element_in_dropdown("//select[@name='view_state']", project.viewstatus)
        self.app.change_value_by_name("description", project.description)

    def count(self):
        wd = self.app.wd
        self.app.return_to_manage_projects()
        return len(wd.find_elements_by_xpath("//table[@class = 'width100']//tr[position()>2]"))
