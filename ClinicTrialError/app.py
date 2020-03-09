from __invoice import Invoice
from __on_running_tasks import tasks

patient = tasks.fetch_patient()
service = tasks.fetch_service()
Invoice.invoice()