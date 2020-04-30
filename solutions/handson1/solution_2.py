top_5_passengers_april = (
    df[["DEST_AIRPORT_ID", "PASSENGERS", "MONTH"]] # select the required columns
    .groupby(["DEST_AIRPORT_ID", "MONTH"]) # group by destination airport id and month
    .sum()
    .query("MONTH == 4") # filter out all other months except april
    .sort_values("PASSENGERS", ascending=False) # sort the aggregated value 
    .iloc[:5]
)
f = plt.figure(figsize=[10, 5])
ax = f.add_subplot()
top_5_passengers_april.plot(kind="bar", ax=ax)