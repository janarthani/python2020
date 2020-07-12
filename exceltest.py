# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:28:27 2020

@author: Janu
"""

# import openpyxl
# FILENAME = "C:\\Users\\Janu\\Desktop\\exceltest\\test1.xlsx"
# WB1 = openpyxl.load_workbook(FILENAME)
# WS1 = WB1.worksheets[0]


import xlwings as xw

WB_PREMIUM_CALC = xw.Book('C://Users//Janu//Desktop//exceltest//resimacprimegenworthpremiumcalculator.xlsm')
WB_TESTCASE_CSV = xw.Book('C://Users//Janu//Desktop//exceltest//product_test_case_507.csv')
SHT_PREMIUM_CALC = WB_PREMIUM_CALC.sheets['PREMIUM']
SHT_TESTCASE_CSV = WB_TESTCASE_CSV.sheets['product_test_case_507']

#sets row and column letter

ROW = 2
TLA_COLUMN = 'J'
TSV_COLUMN = 'K'
BORRPAY_COLUMN = 'L'


# This identifies the cells in the test case CSV


TLA_CELL = TLA_COLUMN + str(ROW)
print(TLA_CELL)

TSV_CELL = TSV_COLUMN + str(ROW)
print(TSV_CELL)

BORRPAY_CELL = BORRPAY_COLUMN + str(ROW)
print(BORRPAY_CELL)

# Sets loan type to New Loan

SHT_PREMIUM_CALC.range('C7').value = 2

# Sets loan Product to Standard

SHT_PREMIUM_CALC.range('C8').value = 1

# Copies total loan amount from csv to premium calculator

SHT_PREMIUM_CALC.range('C10').value = SHT_TESTCASE_CSV.range(TLA_CELL).value

# Sets First Home Buyer to No

SHT_PREMIUM_CALC.range('C14').value = 2
SHT_PREMIUM_CALC.range('C15').value = 1
SHT_PREMIUM_CALC.range('G6').value = 2
SHT_PREMIUM_CALC.range('H6').value = 2
SHT_PREMIUM_CALC.range('I6').value = SHT_TESTCASE_CSV.range(TSV_CELL).value


#copy the result back to the POE test case csv you need to set
#it to a string so it does not coppy the dollar sign.

SHT_TESTCASE_CSV.range(BORRPAY_CELL).value = str(SHT_PREMIUM_CALC.range('I23').value)
