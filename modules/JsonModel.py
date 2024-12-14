from modules import DateTimeService

def json_record_type_00(line):
    return {
        'recordType': line[0:2].strip(),
        'canton': line[2:4].strip(),
        'sslNumber': line[4:19].strip(),
        'creationDate': DateTimeService.convert_to_iso8601_date(line[19:27].strip()),
        'text1': line[27:67].strip(),
        'text2': line[67:107].strip(),
        'codeState': line[107:110].strip()
    }

def json_record_type_06(line):
    return {
        'recordType': line[0:2].strip(),
        'transactionType': line[2:4].strip(),
        'canton': line[4:6].strip(),
        'taxAtSourceCode': line[6:16].strip(),
        'validFrom': DateTimeService.convert_to_iso8601_date(line[16:24].strip()),
        'taxableIncomeFromInCHF': line[24:33].strip(),
        'tariffStepInCHF': line[33:42].strip(),
        'sexCode': line[42:43].strip(),
        'numberOfChildren': int(line[43:45].strip()),
        'minTaxInCHF': line[45:54].strip(),
        'taxRateInPercent': line[54:59].strip(),
        'codeState': line[59:62].strip()
    }

def json_record_type_11(line):
    return {
        'recordType': line[0:2].strip(),
        'transactionType': line[2:4].strip(),
        'canton': line[4:6].strip(),
        'codeTaxType': line[6:16].strip(),
        'validFrom': DateTimeService.convert_to_iso8601_date(line[16:24].strip()),
        'taxableIncomeFromInCHF': line[24:33].strip(),
        'tariffStepInCHF': line[33:42].strip(),
        'sexCode': line[42:43].strip(),
        'numberOfChildren': int(line[43:45].strip()),
        'minTaxInCHF': line[45:54].strip(),
        'taxRateInPercent': line[54:59].strip(),
        'codeState': line[59:62].strip()
    }

def json_record_type_12(line):
    return {
        'recordType': line[0:2].strip(),
        'transactionType': line[2:4].strip(),
        'canton': line[4:6].strip(),
        'codePurchaseCommission': line[6:16].strip(),
        'validFrom': DateTimeService.convert_to_iso8601_date(line[16:24].strip()),
        'taxableIncomeFromInCHF': line[24:33].strip(),
        'tariffStepInCHF': line[33:42].strip(),
        'sexCode': line[42:43].strip(),
        'numberOfChildren': int(line[43:45].strip()),
        'minTaxInCHF': line[45:54].strip(),
        'taxRateInPercent': line[54:59].strip(),
        'codeState': line[59:62].strip()
    }

def json_record_type_13(line):
    return {
        'recordType': line[0:2].strip(),
        'transactionType': line[2:4].strip(),
        'canton': line[4:6].strip(),
        'codeMedianValue': line[6:16].strip(),
        'validFrom': DateTimeService.convert_to_iso8601_date(line[16:24].strip()),
        'taxableIncomeFromInCHF': line[24:33].strip(),
        'tariffStepInCHF': line[33:42].strip(),
        'sexCode': line[42:43].strip(),
        'numberOfChildren': int(line[43:45].strip()),
        'minTaxInCHF': line[45:54].strip(),
        'taxRateInPercent': line[54:59].strip(),
        'codeState': line[59:62].strip()
    }

def json_record_type_99(line):
    return {
        'recordType': line[0:2].strip(),
        'sslNumberSender': line[2:17].strip(),
        'cantonSender': line[17:19].strip(),
        'transmittedRecords': int(line[19:27].strip()),
        'checksumAmount': line[27:36].strip(),
        'codeState': line[36:39].strip()
    }
