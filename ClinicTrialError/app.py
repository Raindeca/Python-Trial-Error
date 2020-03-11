from __invoice import Invoice
from __on_running_tasks import Tasks

bill = Invoice(Tasks.fetch_patient(), Tasks.fetch_service())
app = bill.invoice()
# Invoice.invoice()