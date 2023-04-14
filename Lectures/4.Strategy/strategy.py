from __future__ import annotations
from abc import ABC, abstractmethod


# Use this pattern to change the behavior of an object
# depending on the value of a FIELD
class ImageStorage:
    def __init__(self, compressor:Compressor, filter:Filter):
        self.compressor = compressor
        self.filter = filter

    def store(self, filename: str):
        self.compressor.compress(filename)
        self.filter.apply(filename)


class Compressor(ABC):
    @abstractmethod
    def compress(self, filename: str):
        pass


class JpegCompressor(Compressor):
    def compress(self, filename: str):
        print(f'Compressing {filename} using JPEG!')


class PNGCompressor(Compressor):
    def compress(self, filename: str):
        print(f"Compressing {filename} using PNG!")


class Filter(ABC):
    @abstractmethod
    def apply(self, filename: str):
        pass


class BlackAndWhiteFilter(Filter):
    def apply(self, filename: str):
        print("Applying B&W filter on {filename}!")