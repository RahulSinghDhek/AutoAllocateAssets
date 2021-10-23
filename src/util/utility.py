from src.util import log

logger = log.Logger()


def convertToInt(listOfStrings):
    try:
        return [int(element) for element in listOfStrings]
    except ValueError as err:
        logger.error("Failed to convert string into integer : " + str(err))
        return None


def convertInterestRatesToFloat(listOfInterestRates):
    try:
        return [float(element.split("%")[0]) for element in listOfInterestRates]
    except ValueError as err:
        logger.error("Failed to extract rates from given string values : " + str(err))
        return None
