
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp                            | ip                                   | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:-------------------------------|:-------------------------------------|:-----------------|
|  0 | [5](config/5.json)   | cnah2.lanyunshi.cc  | Turkey        | TR   | Stark Industries Solutions Ltd | 95.164.11.138                        | Yes (Region: TR) |
|  1 | [6](config/6.json)   | 183.233.187.214     | Hong Kong     | HK   | CNSERVERS                      | 172.247.18.74                        | Yes (Region: US) |
|  2 | [7](config/7.json)   | bjcu.xzyunjiasu.icu | United States | US   | PONYNET                        | 209.141.58.10                        | Yes (Region: US) |
|  3 | [8](config/8.json)   | 183.233.187.214     | China         | CN   | CNSERVERS                      | 192.151.223.154                      | Yes (Region: US) |
|  4 | [9](config/9.json)   | 45.199.138.146      | Netherlands   | NL   | YISP B.V.                      | 154.84.1.122                         | Yes (Region: NL) |
|  5 | [14](config/14.json) | 45.58.152.70        | Netherlands   | NL   | SHARKTECH                      | 2610:150:4000:1da:225:90ff:fea7:7db4 | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiY25haDIubGFueXVuc2hpLmNjIiwgImFpZCI6IDIsICJob3N0IjogIiIsICJpZCI6ICIwYjE5MmZmMi03NzE4LTMyMDYtOTNmNC02YTI2MGE0MjJjYzgiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNjAwMTAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWI4OVx1NWZiZFx1NzcwMVx1NmVjMVx1NWRkZVx1NWUwMlx1ODA1NFx1OTAxYSA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNzcwZWU3MzAtMjQ1MC00ZTNjLWE2YzYtMzkzMmJkMzJhZmJkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDM4MjYyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTI1Ni1nY206NWM4YjIxMGEtMmYwMC00MjkyLTk2NGItMDUyODFjN2FkNWQx@bjcu.xzyunjiasu.icu:33952#github.com/freefq%20-%20%E6%B9%96%E5%8D%97%E7%9C%81%E8%81%94%E9%80%9A%207
vmess://eyJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvNWYyZWE1MzEtMjllNC00ODM2LWM2MGEtYTczOWI4ZTZiMGEzIiwgInBvcnQiOiA1NjI2NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1ZTdmXHU0ZTFjXHU3NzAxXHU1ZTdmXHU1ZGRlXHU1ZTAyXHU3OWZiXHU1MmE4IDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICJraW5nLnR1cmJvMDIxLmxpbmsifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA5IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0NiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTE5MzEwMDM4OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTQiLCAiYWRkIjogIjQ1LjU4LjE1Mi43MCIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNTQ5NjQ3NDUueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTE5MzEwMDM4OCIsICJ0bHMiOiAidGxzIn0=
```

