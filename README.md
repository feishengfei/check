
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr              | cn            | cc   | isp       | ip                                   | chatgpt          |
|---:|:---------------------|:------------------|:--------------|:-----|:----------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.110.144     | China         | CN   | PEG-SV    | 142.4.110.137                        | Yes (Region: US) |
|  1 | [3](config/3.json)   | 198.2.202.84      | China         | CN   | PEG-SV    | 142.4.102.244                        | Yes (Region: US) |
|  2 | [5](config/5.json)   | 38.63.0.80        | United States | US   | PEG-SV    | 38.63.0.65                           | Yes (Region: US) |
|  3 | [8](config/8.json)   | www.speedtest.net | Poland        | PL   | OVH SAS   | 54.36.174.181                        | Yes (Region: FR) |
|  4 | [12](config/12.json) | 45.199.138.152    | Netherlands   | NL   | YISP B.V. | 2a02:2a38:1:2796:ae1f:6bff:fe24:8940 | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAyIiwgImFkZCI6ICIxNDIuNC4xMTAuMTQ0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjY4ZDIzOGNlLTNjYTEtNDZkYy1iODMzLWEwOTE2YzgyOWFkMyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODI1MTY1OC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2NTk4MDEzODUxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjg0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk0ODU5NjA1MzIxIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDMiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggNSIsICJhZGQiOiAiMzguNjMuMC44MCIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTk0NTgxNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NjU5ODAxMzg1MSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInd3dy5zcGVlZHRlc3QubmV0IiwgInBvcnQiOiA4MCwgImlkIjogIjYyNTE1YWYyLTFkZDktNDY3Yi05ZGQzLTc3NGFiZWZiNmE2MiIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAiaHUxLnh2MnJheS5uZXQiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMiIsICJhZGQiOiAiNDUuMTk5LjEzOC4xNTIiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTQ2OTBkZDI0IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjMyNTIyMTc4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY1OTgwMTM4NTEiLCAidGxzIjogInRscyJ9
```

