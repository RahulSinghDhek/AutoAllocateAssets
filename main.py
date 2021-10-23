import sys

from src.managers.assetAllocator import AssetAllocator
from src.util import log, constants

logger = log.Logger()


def main():
    if len(sys.argv) < 2:
        logger.error(constants.PATH_ERROR)
        return

    portfolio = None
    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            input_lines = [line.strip() for line in file]
    except IOError as err:
        logger.error(constants.FILE_ERROR + str(err))
        return

    asset_allocator = AssetAllocator(portfolio, input_lines)
    asset_allocator.startSelfAllocation()


if __name__ == "__main__":
    main()
