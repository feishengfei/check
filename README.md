
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp                               | ip                                   | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:----------------------------------|:-------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 45.199.138.191      | Netherlands   | NL   | YISP B.V.                         | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba  | Yes (Region: NL) |
|  1 | [5](config/5.json)   | 45.199.138.146      | Netherlands   | NL   | YISP B.V.                         | 154.84.1.122                         | Yes (Region: NL) |
|  2 | [8](config/8.json)   | bjcu.xzyunjiasu.icu | United States | US   | PONYNET                           | 209.141.58.10                        | Yes (Region: US) |
|  3 | [10](config/10.json) | 45.58.152.70        | Netherlands   | NL   | SHARKTECH                         | 2610:150:4000:1da:225:90ff:fea7:7db4 | Yes (Region: US) |
|  4 | [11](config/11.json) | iepl2.airtcp.vip    | Malaysia      | MY   | TM TECHNOLOGY SERVICES SDN. BHD.  | 175.143.20.137                       | Yes (Region: MY) |
|  5 | [13](config/13.json) | cnah2.lanyunshi.cc  | Turkey        | TR   | Stark Industries Solutions Ltd    | 95.164.11.138                        | Yes (Region: TR) |
|  6 | [15](config/15.json) | 120.233.43.47       | Taiwan        | TW   | Data Communication Business Group | 211.20.157.212                       | Yes (Region: TW) |
|  7 | [19](config/19.json) | 183.233.187.214     | Hong Kong     | HK   | CNSERVERS                         | 172.247.18.74                        | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE5MSIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNDIwNzcyMzAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTI4MDA5OTEzOCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0NiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTE5MzEwMDM4OCIsICJ0bHMiOiAidGxzIn0=
ss://YWVzLTI1Ni1nY206NWM4YjIxMGEtMmYwMC00MjkyLTk2NGItMDUyODFjN2FkNWQx@bjcu.xzyunjiasu.icu:33952#github.com/freefq%20-%20%E6%B9%96%E5%8D%97%E7%9C%81%E8%81%94%E9%80%9A%208
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjQ1LjU4LjE1Mi43MCIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNTQ5NjQ3NDUueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTE5MzEwMDM4OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiaWVwbDIuYWlydGNwLnZpcCIsICJhaWQiOiAyLCAiaG9zdCI6ICIiLCAiaWQiOiAiMGIxOTJmZjItNzcxOC0zMjA2LTkzZjQtNmEyNjBhNDIyY2M4IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDEyMzE2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRlOTFcdTZkNmVcdTVlMDJcdTc5ZmJcdTUyYTggMTEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiY25haDIubGFueXVuc2hpLmNjIiwgImFpZCI6IDIsICJob3N0IjogIiIsICJpZCI6ICIwYjE5MmZmMi03NzE4LTMyMDYtOTNmNC02YTI2MGE0MjJjYzgiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNjAwMTAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWI4OVx1NWZiZFx1NzcwMVx1NmVjMVx1NWRkZVx1NWUwMlx1ODA1NFx1OTAxYSAxMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTUiLCAiYWRkIjogIjEyMC4yMzMuNDMuNDciLCAicG9ydCI6ICIxMTAxMyIsICJpZCI6ICI4NWRiNjY1Mi1hNzQ3LTNhMGEtYTE3MC00MjI3MzYwNzY0MTAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNzcwZWU3MzAtMjQ1MC00ZTNjLWE2YzYtMzkzMmJkMzJhZmJkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDM4MjYyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMTkiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

