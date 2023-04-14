from abc import ABC, abstractmethod

# Good for defining common behavior(template) as well as some extra stuff to override
# in inheriting classes
# like recording things(e.g. Audit Trail)

# We can implement it using both Strategy pattern(polymorphism)
# and inheritance


class AuditTrail:
    # In real world, this method will take a parameter to record 
    # who is performing the action.
    def record(self):
        print("Audit")

class Task(ABC):
    def __init__(self, audit_trail: AuditTrail):
        self.audit_trail = audit_trail

    def execute(self):
        self.audit_trail.record()

        self._do_execute()
    
    @abstractmethod
    def _do_execute(self):
        pass


class TransferMoneyTask(Task):
    def _do_execute(self):
        # Logic for transferring money
        print("Transfer money")



class GenerateReportTask(Task):
        def _do_execute(self):
            # Logic for report generation
            print("Generate report")