# MealBot
稼働中:
[rkun on Twitter](https://twitter.com/rkunkunr)

毎朝7:00につぶやきます。VPSを借りたのでVPSで運用中。

## fix.jsonについて
- 不定期のルールを作るときにfix.jsonに書き込む。
- 範囲指定とピンポイント指定ができる。
- 範囲指定の場合、rangeプロパティにTrueを、ピンポイント指定の場合、rangeにFalseを。
- 範囲指定ならstartとendに、ピンポイントならdateに`%Y/%m/%d`のフォーマットで指定。
