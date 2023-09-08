df_outgoing = df[["ORIGIN_AIRPORT_ID", "PASSENGERS"]].groupby("ORIGIN_AIRPORT_ID").sum()
df_outgoing = df_outgoing.reset_index().rename({"PASSENGERS": "OUTGOING"}, axis=1)
df_incoming =  df[["DEST_AIRPORT_ID", "PASSENGERS"]].groupby("DEST_AIRPORT_ID").sum()
df_incoming = df_incoming.reset_index().rename({"PASSENGERS": "INCOMING"}, axis=1)

# merge the two crafted dataframe using  the left_on and the right_on parameter of the merge
# pay attention the merging strategy is inner join
df_out_incom = pd.merge(df_outgoing, df_incoming, left_on="ORIGIN_AIRPORT_ID", right_on="DEST_AIRPORT_ID")

df_out_incom["DIFF"] = df_out_incom["OUTGOING"] - df_out_incom["INCOMING"]

df_out_incom.query("DIFF == 0 and OUTGOING > 0")
