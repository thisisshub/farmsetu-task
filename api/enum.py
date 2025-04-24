from enum import Enum

class RegionEnum(Enum):
    UK = "UK"
    England = "England"
    Wales = "Wales"
    Scotland = "Scotland"
    Northern_Ireland = "Northern_Ireland"
    England_and_Wales = "England_and_Wales"
    England_N = "England_N"
    England_S = "England_S"
    Scotland_N = "Scotland_N"
    Scotland_E = "Scotland_E"
    Scotland_W = "Scotland_W"
    England_E_and_NE = "England_E_and_NE"
    England_NW_and_N_Wales = "England_NW_and_N_Wales"
    Midlands = "Midlands"
    East_Anglia = "East_Anglia"
    England_SW_and_S_Wales = "England_SW_and_S_Wales"
    England_SE_and_Central_S = "England_SE_and_Central_S"
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
class ParameterEnum(Enum):
    Tmax = "Tmax"
    Tmin = "Tmin"
    Tmean = "Tmean"
    Sunshine = "Sunshine"
    Rainfall = "Rainfall"
    Raindays1mm = "Raindays1mm"
    AirFrost = "AirFrost"
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
class MonthEnum(Enum):
    jan = "jan"    
    feb = "feb"    
    mar = "mar"    
    apr = "apr"    
    may = "may"    
    jun = "jun"    
    jul = "jul"    
    aug = "aug"    
    sep = "sep"    
    oct = "oct"    
    nov = "nov"    
    dec = "dec"     
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
class SeasonEnum(Enum):
    win = "win"     
    spr = "spr"     
    sum = "sum"     
    aut = "aut"     
    ann = "ann"
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]