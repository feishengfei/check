
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr               | cn          | cc   | isp                               | ip                                   | chatgpt          |
|---:|:---------------------|:-------------------|:------------|:-----|:----------------------------------|:-------------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 183.233.187.214    | Hong Kong   | HK   | CNSERVERS                         | 172.247.18.74                        | Yes (Region: US) |
|  1 | [5](config/5.json)   | cnah2.lanyunshi.cc | Turkey      | TR   | Stark Industries Solutions Ltd    | 95.164.11.138                        | Yes (Region: TR) |
|  2 | [6](config/6.json)   | 45.199.138.146     | Netherlands | NL   | YISP B.V.                         | 154.84.1.122                         | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 45.58.152.70       | Netherlands | NL   | SHARKTECH                         | 2610:150:4000:1da:225:90ff:fea7:7db4 | Yes (Region: US) |
|  4 | [15](config/15.json) | 120.233.43.47      | Taiwan      | TW   | Data Communication Business Group | 211.20.157.213                       | Yes (Region: TW) |

## Valid
```
vmess://eyJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNzcwZWU3MzAtMjQ1MC00ZTNjLWE2YzYtMzkzMmJkMzJhZmJkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDM4MjYyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTEyLjI5Ljk0LjIzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMjFhOWJmZjItNzJkZS00ZTYyLTkzZmYtOGIxNTlmNjZkODc1IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ5MDA2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiY25haDIubGFueXVuc2hpLmNjIiwgImFpZCI6IDIsICJob3N0IjogIiIsICJpZCI6ICIwYjE5MmZmMi03NzE4LTMyMDYtOTNmNC02YTI2MGE0MjJjYzgiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNjAwMTAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWI4OVx1NWZiZFx1NzcwMVx1NmVjMVx1NWRkZVx1NWUwMlx1ODA1NFx1OTAxYSA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0NiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTE5MzEwMDM4OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiNDUuNTguMTUyLjcwIiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41NDk2NDc0NS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5MTkzMTAwMzg4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTUiLCAiYWRkIjogIjEyMC4yMzMuNDMuNDciLCAicG9ydCI6ICIxMTAxMyIsICJpZCI6ICI4NWRiNjY1Mi1hNzQ3LTNhMGEtYTE3MC00MjI3MzYwNzY0MTAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

