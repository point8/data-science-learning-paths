import os
import subprocess
import zipfile

import numpy
import pandas


def read_usa_temperature(data_path="../.assets/data/climate/usa-avg-temp-monthly.csv"):
    def fahrenheit_to_celsius(f):
        c = (f - 32) * 5 / 9
        return c

    usa_temp = pandas.read_csv(data_path, dtype={"Date": "str"})
    # get parsable date format
    usa_temp["Date"] = usa_temp["Date"].apply(lambda s: f"{s[:4]}-{s[4:]}")
    # convert units
    usa_temp["Value"] = usa_temp["Value"].apply(fahrenheit_to_celsius)
    usa_temp["Anomaly"] = usa_temp["Anomaly"].apply(fahrenheit_to_celsius)
    # datetime index
    usa_temp["Date"] = pandas.to_datetime(usa_temp["Date"])
    usa_temp = usa_temp.set_index("Date")
    return usa_temp


def read_chicago_taxi_trips(data_path, freq="d"):
    taxi_data = pandas.read_csv(
        data_path, parse_dates=["Trip Start Timestamp", "Trip End Timestamp"]
    )
    taxi_data = taxi_data.set_index("Trip Start Timestamp")
    taxi_trips = taxi_data.resample(freq).size()
    taxi_trips.freq = freq
    return taxi_trips


def read_chicago_taxi_trips_daily(
    data_path="../.assets/data/taxi/taxi_trips_daily.csv",
):
    taxi_trips = pandas.read_csv(data_path, sep=";", parse_dates=["Date"])
    taxi_trips = taxi_trips.set_index("Date")
    # taxi_trips["Trips"].freq = pandas.Timedelta('1 day')
    return taxi_trips


def read_iris(data_path="../.assets/data/iris/iris.csv"):
    data = pandas.read_csv(data_path, sep=",")
    return data


def read_house_prices(
    data_path="../.assets/data/house/prices.csv",
    encode_ordinal=True,
    drop_sparse=True,
    encode_categorial=True,
    drop_first_level=False,
):
    target = "SalePrice"
    numeric = [
        "2ndFlrSF",
        "LotArea",
        "OverallQual",
        "OverallCond",
        "YearBuilt",
        "YearRemodAdd",
        "BsmtFinSF1",
        "BsmtFinSF2",
        "1stFlrSF",
        "2ndFlrSF",
        "LowQualFinSF",
        "GrLivArea",
        "BsmtFullBath",
        "BsmtHalfBath",
        "FullBath",
        "HalfBath",
        "TotRmsAbvGrd",
        "Fireplaces",
        "GarageCars",
        "GarageArea",
        "EnclosedPorch",
        "PoolArea",
        "YrSold",
    ]
    ordinal = [
        "HeatingQC",
        "BsmtQual",
        "BsmtCond",
        "ExterQual",
        "ExterCond",
        "KitchenQual",
        "FireplaceQu",
        "GarageQual",
        "GarageCond",
    ]
    categorial = [
        "MSSubClass",
        "MSZoning",
        "Street",
        "LotShape",
        "LandContour",
        "Utilities",
        "LotConfig",
        "LandSlope",
        "Neighborhood",
        "Condition1",
        "Condition2",
        "BldgType",
        "HouseStyle",
        "RoofStyle",
        "RoofMatl",
        "Exterior1st",
        "Exterior2nd",
        "MasVnrType",
        "Foundation",
        "BsmtExposure",
        "BsmtFinType1",
        "BsmtFinType2",
        "Heating",
        "CentralAir",
        "Electrical",
        "Functional",
        "GarageType",
        "GarageFinish",
        "PavedDrive",
        "MoSold",
        "SaleType",
        "SaleCondition",
    ]
    # features rejected because of many missing values
    sparse = [
        "3SsnPorch",
        "ScreenPorch",
        "Alley",
        "PoolQC",
        "MiscFeature",
        "Fence",
        "LotFrontage",
        "GarageYrBlt",
        "MasVnrArea",
        "WoodDeckSF",
        "OpenPorchSF",
    ]
    categorial_selected = [
        "MSSubClass",
        "LandSlope",
        "BldgType",
        "HouseStyle",
        "Foundation",
        "Heating",
        "CentralAir",
        "Functional",
    ]
    # read file
    data = pandas.read_csv(data_path)
    data = data.drop("Id", axis="columns")
    # encode ordinal
    qual_dict = {"Ex": 1, "Gd": 2, "TA": 3, "Fa": 4, "Po": 5, "NA": 6, numpy.nan: 6}
    if drop_sparse:
        data = data[data.columns.difference(sparse)]
    if encode_ordinal:
        data[ordinal] = data[ordinal].replace(qual_dict)
    # encode categorial
    if encode_categorial:
        data_cat = pandas.get_dummies(
            data[categorial_selected], drop_first=drop_first_level
        )
        data = pandas.concat(
            [
                data[data.columns.difference(categorial + [target])],
                data_cat,
                data[target],
            ],
            axis=1,
        )
    return data


def read_titanic(data_path="../.assets/data/titanic/titanic.csv"):
    data = pandas.read_csv(data_path)
    return data


def read_house_prices_seattle(
    data_path="../.assets/data/houses_seattle/kc_house_data.csv",
    descr_path="../.assets/data/houses_seattle/description.csv",
):
    data = pandas.read_csv(data_path, sep=",", parse_dates=["date"])
    data_descr = pandas.read_csv(descr_path, sep=", ")
    return data, data_descr
