#!/usr/bin/env python3
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv

#フォーマット文字列の作成
html_body = """
    <html><body>
    <img src="oneday.png">
    <img src="third.png"> 
    </body></html>"""

print("Content-type: text/html\n")

##---グラフ生成処理---
#sensorData.csvをdata_listに格納
data_list = pd.read_csv("../sensorData.csv").values.tolist()

#在室判定
i = 0
for i in range(len(data_list)):
    if data_list[i][2] > 400:
        data_list[i][2] = 1
    else: data_list[i][2] = 0

#listの初期化
day_x = []
day_y = []
third_x = []
third_y = []
#1日分のデータを抽出
oneday = 150
while oneday >= 0:
    day_x.append(data_list[i-oneday][0])
    day_y.append(data_list[i-oneday][2])
    oneday -= 1
#3日分のデータを抽出
third = 450
while third >= 0:
    third_x.append(data_list[i-third][0])
    third_y.append(data_list[i-third][2])
    third -= 1

##グラフの描写(1日の在室判定(24時間))
#グラフタイトル
plt.title("Determination of occupancy in one day")
#グラフの軸
plt.xlabel("Time")
plt.xticks( [0,149],[day_x[0],day_x[149]] )
plt.ylabel("Judgment(0:absence,1:Presence)")
plt.yticks( [0,1] )
#グラフを生成
plt.plot(day_x,day_y)
#グラフを表示
plt.tight_layout()
plt.show()
#グラフを画像保存
plt.savefig('../oneday.png')

#グラフの大きさ指定
plt.figure(figsize=(10,5))
##グラフの描写(3日間のグラフ(1日の在室合計時間))
plt.title("3-day determination of occupancy")
#グラフの軸  
plt.xlabel("Time")
plt.xticks( [0,149,299,449,],[third_x[0],third_x[149],third_x[299],third_x[449]] )
plt.ylabel("Judgment(0:absence,1:Presence)")
plt.yticks( [0,1] )
#グラフを生成
plt.plot(third_x,third_y)
#グラフを表示                                            
plt.show()
#グラフを画像保存
plt.savefig('../third.png')


