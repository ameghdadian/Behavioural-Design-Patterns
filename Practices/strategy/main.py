from chat_client import ChatClient, AesEncryption, DesEncryption


def main():
    client = ChatClient(AesEncryption())
    client.send("Hey buddy, what's going on?")

    client2 = ChatClient(DesEncryption())
    client2.send("I'm fine, thanks for asking!")


main()