from datetime import datetime, timedelta


def stringifiedDate(datetimeToDisplay):
    return f"{datetimeToDisplay.month}/{datetimeToDisplay.day}/{datetimeToDisplay.year}"


TODAY = datetime.now()
NEXT_WEEK = TODAY + timedelta(days=7)
LAST_WEEK = TODAY - timedelta(days=7)
DATE_PATTERN_4_DIGIT_YEAR = "[0-9]+/[0-9]+/[0-9]{4}"
DATE_PATTERN_2_DIGIT_YEAR = "[0-9]+/[0-9]+/[0-9]{2}"


def stringifiedDateForFileName(datetimeToDisplay):
    return f"{datetimeToDisplay.month}_{datetimeToDisplay.day}_{datetimeToDisplay.year}"


def getDogCountsByFoster(listOfDogs):
    fosters = dict()
    for dog in listOfDogs:
        foster = dog.foster
        if fosters.get(foster):
            fosters[foster].append(dog)
        else:
            fosters[foster] = [dog]
    return fosters

def dateBetween(canidateDate, start, end):
    return canidateDate >= start and canidateDate <= end