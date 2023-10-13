
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn            | cc   | isp        | ip             | chatgpt          |
|---:|:---------------------|:----------------------------|:--------------|:-----|:-----------|:---------------|:-----------------|
|  0 | [5](config/5.json)   | 156.225.67.104              | Netherlands   | NL   | YISP B.V.  | 154.84.1.44    | Yes (Region: NL) |
|  1 | [6](config/6.json)   | 45.199.138.186              | Netherlands   | NL   | YISP B.V.  | 154.84.1.122   | Yes (Region: NL) |
|  2 | [7](config/7.json)   | us02.shawbrothersstudio.com | United States | US   | NETLAB-SDN | 154.40.56.206  | Yes (Region: US) |
|  3 | [8](config/8.json)   | 183.238.202.173             | Hong Kong     | HK   | CNSERVERS  | 156.227.19.218 | Yes (Region: US) |
|  4 | [13](config/13.json) | 45.199.138.222              | Netherlands   | NL   | YISP B.V.  | 154.84.1.122   | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY5NDQ4MDY5NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xODYiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTY1OTgwMTM4NTEiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpoZzloNUtwTW1KTGxpNlc2UWpkMnlp@us02.shawbrothersstudio.com:43642#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E6%96%B0%E5%9B%BD%E4%BF%A1%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%207
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggOCIsICJhZGQiOiAiMTgzLjIzOC4yMDIuMTczIiwgInBvcnQiOiAiNTE5MDQiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMyIsICJhZGQiOiAiNDUuMTk5LjEzOC4yMjIiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NjI1MTY5MzA0OCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

