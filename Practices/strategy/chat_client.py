from __future__ import annotations
from abc import ABC, abstractmethod


class ChatClient:
    def __init__(self, encryption_alg: EncryptionType):
        self.encryption_alg = encryption_alg

    def send(self, message: str):
        self.encryption_alg.encrypt(message)

        print("Sending the encrypted message...")


class EncryptionType(ABC):
    @abstractmethod
    def encrypt(self, message):
        pass


class DesEncryption(EncryptionType):
    SALT_KEY = 1
    def encrypt(self, message):
        print(f"Encrypting '{message}' using DES algorithm!")
        new_message = self._encrypt(message)
        print(f"Encrypted message: {new_message}")
    
    def _encrypt(self, message: str):
        new_message = ""
        for ch in message:
            new_ch = chr(ord(ch) + self.SALT_KEY)
            new_message += new_ch

        return new_message



class AesEncryption(EncryptionType):
    SALT_KEY = 2
    def encrypt(self, message):
        print(f"Encrypting '{message}' using AES algorithm!")
        new_message = self._encrypt(message)
        print(f"Encrypted message: {new_message}")

    def _encrypt(self, message: str):
        new_message = ""
        for ch in message:
            new_ch = chr(ord(ch) + self.SALT_KEY)
            new_message += new_ch

        return new_message
