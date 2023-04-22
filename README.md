
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn     | cc   | isp                         | ip             | chatgpt          |
|---:|:---------------------|:-----------------|:-------|:-----|:----------------------------|:---------------|:-----------------|
|  0 | [1](config/1.json)   | 20.222.195.170   | Japan  | JP   | MICROSOFT-CORP-MSN-AS-BLOCK | 20.222.195.170 | Yes (Region: JP) |
|  1 | [9](config/9.json)   | 37.120.209.124   | Sweden | SE   | M247 Europe SRL             | 37.120.209.122 | Yes (Region: SE) |
|  2 | [12](config/12.json) | cf.noaries.de    |        |      |                             | 107.189.28.253 | Yes (Region: LU) |
|  3 | [16](config/16.json) | sz.cny.page      | Taiwan | TW   | Kaopu Cloud HK Limited      | 38.54.107.182  | Yes (Region: TW) |
|  4 | [17](config/17.json) | sz.cny.page      | Japan  | JP   | G-Core Labs S.A.            | 31.223.184.252 | Yes (Region: JP) |
|  5 | [20](config/20.json) | steam.dnspro.icu | Turkey | TR   | Bogahost Bilişim            | 5.180.32.144   | Yes (Region: TR) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRNaWNyb3NvZnRcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMSIsICJhZGQiOiAiMjAuMjIyLjE5NS4xNzAiLCAicG9ydCI6ICI4MCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiYTY4OTk1NTMtNjFkYi0zNmI1LWFhM2MtMmVhOWEzZmJlODYzIiwgImFpZCI6ICIyIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi90N3c5MmozODlmdnloMzh2YmgiLCAiaG9zdCI6ICIyMC4yMjIuMTk1LjE3MCIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmNTdcdTlhNmNcdTVjM2NcdTRlOWEgIDkiLCAiYWRkIjogIjM3LjEyMC4yMDkuMTI0IiwgInBvcnQiOiAiMzE5ODkiLCAiaWQiOiAiZGMwY2YyMmQtZTM1Yy00Yjc3LTg5MjQtOTc3ZjY4NDQ5MDliIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAiODA4MCIsICJpZCI6ICI2ZjFkOTY4ZS03ZjQxLTQxZmQtOTMxZC03M2NmMzVhOWYyNmIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImJ1eXZtLmlpaW8ud2lraSIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiJ9
ss://YWVzLTEyOC1nY206MmNmYzRjNTgtODhjYi00ZTAwLTk5NzctZWYwYTM3NTU5YTIy@sz.cny.page:11536#github.com/freefq%20-%20%E6%B5%B7%E5%8D%97%E7%9C%81%E6%B5%B7%E5%8F%A3%E5%B8%82%E7%94%B5%E4%BF%A1%2016
ss://YWVzLTEyOC1nY206MmNmYzRjNTgtODhjYi00ZTAwLTk5NzctZWYwYTM3NTU5YTIy@sz.cny.page:32366#github.com/freefq%20-%20%E6%B5%B7%E5%8D%97%E7%9C%81%E6%B5%B7%E5%8F%A3%E5%B8%82%E7%94%B5%E4%BF%A1%2017
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTY1YjBcdTU2ZmRcdTRmZTFcdTkwMWFcdTRmZTFcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggMjAiLCAiYWRkIjogInN0ZWFtLmRuc3Byby5pY3UiLCAicG9ydCI6ICI1MDAwIiwgImlkIjogIjcxN2U2MDAxLWM0MGYtM2NiYS04NzYzLTYyMzY2MWE1MzczNyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAic3RlYW0uZG5zcHJvLmljdSIsICJwYXRoIjogIi9pc28iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

