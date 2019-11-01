import sys
import re
import datetime

# adb shell dumpsys alarm
# 上の結果からエポックタイムを見やすい日時に変換するだけ

args = sys.argv

# sample_file.txtファイルを"読み込みモード"で開く
file_data = open(args[1], "r")

pattern = r'(?<=when )\d+'

# 読み込んだテキストファイルを１行ずつ表示
for line in file_data:
    result = re.search(pattern, line)
    if result: #none以外の場合
        unixMs = int(result.group(0))
        unixSeconds = unixMs/1000
        if unixSeconds < 2147483647:
            dt = datetime.datetime.fromtimestamp(unixSeconds)
            dtstr = dt.strftime('%Y-%m-%d %H:%M:%S')
            print(str(unixMs)+' '+dtstr)
  
# 開いたファイルを閉じる
file_data.close()