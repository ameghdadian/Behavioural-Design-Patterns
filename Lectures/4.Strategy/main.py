from strategy import (
    ImageStorage,
    JpegCompressor,
    BlackAndWhiteFilter
)


def main():
    imageStorage = ImageStorage(
        JpegCompressor(),
        BlackAndWhiteFilter(),
    )
    imageStorage.store('a')

main()