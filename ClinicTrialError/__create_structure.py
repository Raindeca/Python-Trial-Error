from __on_running_tasks import Tasks
from __patients import Patients
from __services import Services

class Create_Structure:

    def patient():
        Tasks.fetch_patient()

    def service():
        Tasks.fetch_service()