# create a new feature (column) for the dataset using the origin and destination
df["ROUTE"] = (
    df[["ORIGIN_AIRPORT_ID", "DEST_AIRPORT_ID"]]
    .apply(lambda x: "_".join([str(y) for y in x]), axis=1, raw=True)
)

aggreg_most_crowded = (
    df[["ROUTE", "MAIL", "FREIGHT", "PASSENGERS"]] # select the required columns
    .groupby(["ROUTE"]) # group by the new ROUTE column
    .sum()
)

# get the top 1 route and take the index
idx_mail = aggreg_most_crowded.MAIL.sort_values(ascending=False).index[0]
# use the original dataset with the route column, set ROUTE as index and locate the one of interest
df.set_index("ROUTE").loc[idx_mail][["ORIGIN", "DEST"]].iloc[0]

idx_pass = aggreg_most_crowded.PASSENGERS.sort_values(ascending=False).index[0]
df.set_index("ROUTE").loc[idx_pass][["ORIGIN", "DEST"]].iloc[0]

idx_freight = aggreg_most_crowded.FREIGHT.sort_values(ascending=False).index[0]
df.set_index("ROUTE").loc[idx_freight][["ORIGIN", "DEST"]].iloc[0]
