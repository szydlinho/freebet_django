from tables.models import Matches_Pred
import pandas as pd


tmp_data=pd.read_csv('C:/Users/szydlikp/django_test/tables/pred.csv',sep=',',
                     usecols=["date", "league", "HomeTeam", "AwayTeam", "model",
                              "prediction", "Result", "result_binary", "corrected"])

tmp_data = tmp_data.fillna('')
#ensure fields are named~ID,Product_ID,Name,Ratio,Description
#concatenate name and Product_id to make a new field a la Dr.Dee's answer
matches = [
    Matches_Pred(
        date = tmp_data.iloc[row]['date'],
        league = tmp_data.iloc[row]['league'],
        HomeTeam = tmp_data.iloc[row]['HomeTeam'],
        AwayTeam = tmp_data.iloc[row]['AwayTeam'],
        model = tmp_data.iloc[row]['model'],
        prediction = tmp_data.iloc[row]['prediction'],
        Result = tmp_data.iloc[row]['Result'],
        result_binary = tmp_data.iloc[row]['result_binary'],
        corrected = tmp_data.iloc[row]['corrected'],
    )
    for row in tmp_data.index
]
Matches_Pred.objects.bulk_create(matches)