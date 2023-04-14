from command import CustomerService, AddCustomerCommand, Button


def main():
    service = CustomerService()
    command = AddCustomerCommand(service)
    button = Button(command)

    button.click()


if __name__ == "__main__":
    main()