from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class WavFile:
    def __init__(self):
        self.segments:List[Segment] = []

    @staticmethod
    def read(filename: str):
        wavFile = WavFile()
        wavFile.segments.append(FormatSegment())
        wavFile.segments.append(FactSegment())
        wavFile.segments.append(FactSegment())
        wavFile.segments.append(FactSegment())

        return wavFile
    
    def execute(self, operation: Operation):
        for segment in self.segments:
            segment.execute(operation)

   
class Segment(ABC):
    @abstractmethod
    def execute(self, opreation: Operation):
        pass


class FormatSegment(Segment):
    def execute(self, opreation: Operation):
        opreation.apply_format_segment(self)


class FactSegment(Segment):
    def execute(self, opreation: Operation):
        opreation.apply_fact_segment(self)


class Operation(ABC):
    @abstractmethod
    def apply_fact_segment(self, segment: FactSegment):
        pass

    @abstractmethod
    def apply_format_segment(self, segment: FormatSegment):
        pass


class NoiseReduction(Operation):
    def apply_fact_segment(self, segment: FactSegment):
        print("Applying noise reduction on fact segment")

    def apply_format_segment(self, segment: FormatSegment):
        print("Applying noise reduction on format segment")


class ReverbAdding(Operation):
    def apply_fact_segment(self, segment: FactSegment):
        print("Applying reverbing on fact segment")

    def apply_format_segment(self, segment: FormatSegment):
        print("Applying reverbing on format segment")


class Normalize(Operation):
    def apply_fact_segment(self, segment: FactSegment):
        print("Applying normalize on fact segment")

    def apply_format_segment(self, segment: FormatSegment):
        print("Applying normalize on format segment")


def main():
    wavfile = WavFile.read("new.wav")
    wavfile.execute(Normalize())
    wavfile.execute(NoiseReduction())
    wavfile.execute(ReverbAdding())



if __name__ == '__main__':
    main()