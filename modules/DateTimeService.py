from datetime import datetime
import locale

def convert_to_locale_date(dateString, localeName='de_CH'):
    # Set the locale to Swiss German (or any other locale you prefer)
    locale.setlocale(locale.LC_TIME, localeName)

    # Parse the input date string in the format YYYYMMDD
    dateObject = datetime.strptime(dateString, "%Y%m%d")

    # Format the date into the locale-specific format
    return dateObject.strftime("%x")  # %x gives the locale's appropriate date representation

def convert_to_iso8601_date(dateString):
    # Parse the input date string in the format YYYYMMDD
    date_object = datetime.strptime(dateString, "%Y%m%d")

    # Format the date into ISO 8601 format YYYY-MM-DD
    return date_object.strftime("%Y-%m-%d")