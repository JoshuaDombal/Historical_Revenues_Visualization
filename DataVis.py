# This file creates a visualization from an excel file of Revenue Data


import matplotlib.pyplot as plt
import pandas as pd
import csv


data = pd.read_excel('Historical_Revenues.xlsx')


print(data.describe())