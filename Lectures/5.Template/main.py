from template import TransferMoneyTask, AuditTrail

def main():
    task = TransferMoneyTask(AuditTrail())
    task.execute()

main()