import random

roczniki = [1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004]

max_index = len(roczniki)-1

szczesliwy_rocznik_index = random.randint(0,max_index)

print(f'Wylosowany szczęśliwy rocznik to: {roczniki[szczesliwy_rocznik_index]}')