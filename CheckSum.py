print("チェックサムの文字列を入力してください")

# ターミナルから文字列情報を取得する
val = input()
# ord(<文字列>)で一文字ごとのアスキーコードのリストを作って
# それをsum([<List>])で合計して、16進数化して出力
print(hex(sum([ord(c) for c in val])))
