import pandas as pd
import os

os.chdir(os.path.dirname(__file__))
df = pd.read_csv("socialMedia.csv")


df[["AgeGroup", "Likes"]].to_csv("SocialMediaBox.csv", index=False)

avg_df = (
    df.groupby(["Platform", "PostType"])["Likes"]
      .mean()
      .round(2)
      .reset_index()
      .rename(columns={"Likes": "AvgLikes"})
)

avg_df.to_csv("SocialMediaAvg.csv", index=False)

time_df = (
    df.groupby("Date")["Likes"]
      .mean()
      .reset_index()
      .rename(columns={"Likes": "AvgLikes"})
)

time_df.to_csv("SocialMediaTime.csv", index=False)