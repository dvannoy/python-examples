import pandas as pd

# create series from list
cities = ["San Diego", "Los Angeles", "San Francisco", "Seattle", "Austin", "Chicago", "Boston"]
s = pd.Series(cities)
print(s.values)
print(s.index)


# create series from dict, will have named index
cities_dict = {"San Diego": "Americas finest city",
               "Los Angeles": "City of Angels",
               "San Francisco": "Tech capital",
               "Seattle": "Rainy as hell",
               "Chicago": "Da Bears"}
s2 = pd.Series(cities_dict)
print(s2.values)
print(s2.index)
print(s2.dtype)

# series of numbers
sales  = [150, 250.50, 10.50, 5.0]
stores = ["Downtown", "Uptown", "North", "South"]
manager = ["Bob", "Jen", "Alan", "Kate"]
s3 = pd.Series(sales, index=stores)
print(s3)
print(s3.sum())
print(s3.count(), s3.mean(), s3.median(), s3.std()) # ignores missing values
print(s3.min(), s3.idxmin()) # idxmin returns index position with min value
print(s3.max(), s3.idxmax()) # idxmax returns index position with max value
print(s3.describe())
print(s3.is_unique)

#apply will call a function on every record
tax = s3.apply(lambda t: t * .10)
print(tax)

# map will replace values by looking up new values in another series (series1.value maps to series2.index)
s4 = pd.Series(stores)
new_s4 = s4.map(pd.Series(manager, index=stores))
print(new_s4)

# read_csv as series
# s4 = pd.read_json("../data/vehicle_stops.jsonl", squeeze = True)
# print(s4)
# print(s4.head)
# print(s4.tail)


#############################################################
# DataFrames
#############################################################
# read_csv as dataframe (many more read options to check out)
try:
    df = pd.read_json("file:///Users/dustinvannoy/dev/python-examples/data/vehicle_stops.jsonl", lines=True)
except ValueError as e:
    print("Ignoring error, likely issues with end of file: {}", e)
print("Num rows %s, Num dimensions %s, Num rows/cols %s" % (len(df), df.ndim, df.shape))

print(df.head())
#
# print(df.sort_values('subject_age', ascending=False).head())

val_cnts = df["subject_age"].value_counts()
print(val_cnts.head())

# replace missing values
df["subject_age"].fillna(0, inplace=True)

df["subject_age"] = df["subject_age"].replace("No Age", 0).astype("int")

df.sort_values("subject_age", ascending=False)
df["subject_age"].head()
# modify column in place
df["subject_age"].add(1)  # or df["subject_age"] + 1
df["subject_age"].head()

# add column (will overwrite if column already exists)
df["new_col"] = df["subject_age"] + 1

# add at speific location
df.insert(0, column = "new_col2", value = "new")

df["sd_resident"].fillna("Unknown")

val_cnts = df["sd_resident"].value_counts()
print(val_cnts.head())
