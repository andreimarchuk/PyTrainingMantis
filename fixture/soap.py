from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        try:
            l = []
            raw_list = client.service.mc_projects_get_user_accessible(username, password)
            for element in raw_list:
                id = element.id
                projectname = element.name
                description = element.description
                l.append(Project(id=id, projectname=projectname, description=description))
            return list(l)

        except WebFault:
            return False