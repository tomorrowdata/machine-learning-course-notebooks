top_5_distance = (
    df[["UNIQUE_CARRIER", "DISTANCE"]] # select only the carrier code and the distance
    .groupby("UNIQUE_CARRIER") # group by distance and apply an aggregation operator
    .sum()
    .sort_values("DISTANCE", ascending=False) # sort the aggregated value 
    .iloc[:5]
)

f = plt.figure(figsize=[10, 5])
ax = f.add_subplot()
top_5_distance.plot(kind="bar", ax=ax)