
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                               | ip                                   | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:----------------------------------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | www.dongtaiwang4.com     | United States | US   | LIMESTONENETWORKS                 | 64.31.55.7                           | Yes (Region: US) |
|  1 | [3](config/3.json)   | bjcu.xzyunjiasu.icu      | United States | US   | PONYNET                           | 209.141.58.10                        | Yes (Region: US) |
|  2 | [6](config/6.json)   | 183.233.187.214          | China         | CN   | CNSERVERS                         | 192.151.223.154                      | Yes (Region: US) |
|  3 | [7](config/7.json)   | 45.199.138.191           | Netherlands   | NL   | YISP B.V.                         | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba  | Yes (Region: NL) |
|  4 | [9](config/9.json)   | 45.58.152.70             | Netherlands   | NL   | SHARKTECH                         | 2610:150:4000:1da:225:90ff:fea7:7db4 | Yes (Region: US) |
|  5 | [14](config/14.json) | tg_mfbpn_d4.52vpn.eu.org | Taiwan        | TW   | Data Communication Business Group | 211.20.157.213                       | Yes (Region: TW) |

## Valid
```
ss://YWVzLTI1Ni1nY206ZG9uZ3RhaXdhbmcuY29t@www.dongtaiwang4.com:26600#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%BE%97%E5%85%8B%E8%90%A8%E6%96%AF%E5%B7%9E%E8%BE%BE%E6%8B%89%E6%96%AFLimestone%E7%BD%91%E7%BB%9C%E5%85%AC%E5%8F%B8%202
ss://YWVzLTI1Ni1nY206NWM4YjIxMGEtMmYwMC00MjkyLTk2NGItMDUyODFjN2FkNWQx@bjcu.xzyunjiasu.icu:33952#github.com/freefq%20-%20%E6%B9%96%E5%8D%97%E7%9C%81%E8%81%94%E9%80%9A%203
vmess://eyJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvNWYyZWE1MzEtMjllNC00ODM2LWM2MGEtYTczOWI4ZTZiMGEzIiwgInBvcnQiOiA1NjI2NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1ZTdmXHU0ZTFjXHU3NzAxXHU1ZTdmXHU1ZGRlXHU1ZTAyXHU3OWZiXHU1MmE4IDYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICJraW5nLnR1cmJvMDIxLmxpbmsifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA3IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE5MSIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNDIwNzcyMzAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTI4MDA5OTEzOCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJhZGQiOiAiNDUuNTguMTUyLjcwIiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41NDk2NDc0NS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5MTkzMTAwMzg4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTQiLCAiYWRkIjogInRnX21mYnBuX2Q0LjUydnBuLmV1Lm9yZyIsICJwb3J0IjogIjExMDEzIiwgImlkIjogIjg1ZGI2NjUyLWE3NDctM2EwYS1hMTcwLTQyMjczNjA3NjQxMCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

