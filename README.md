
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn            | cc   | isp                               | ip                                   | chatgpt          |
|---:|:---------------------|:----------------------|:--------------|:-----|:----------------------------------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 198.2.202.84          | China         | CN   | PEG-SV                            | 142.4.102.244                        | Yes (Region: US) |
|  1 | [5](config/5.json)   | 198.2.202.88          | China         | CN   | PEG-SV                            | 142.4.102.244                        | Yes (Region: US) |
|  2 | [6](config/6.json)   | 67.21.90.5            | United States | US   | SHARKTECH                         | 107.167.22.10                        | Yes (Region: US) |
|  3 | [7](config/7.json)   | jscm01.celerlink.one  | Taiwan        | TW   | Data Communication Business Group | 111.250.2.157                        | Yes (Region: TW) |
|  4 | [8](config/8.json)   | 46caadb.f2.gladns.com | Poland        | PL   | OVH SAS                           | 54.36.174.181                        | Yes (Region: FR) |
|  5 | [18](config/18.json) | 45.199.138.152        | Netherlands   | NL   | YISP B.V.                         | 2a02:2a38:1:2796:ae1f:6bff:fe24:8940 | Yes (Region: NL) |
|  6 | [20](config/20.json) | sneed-a.v2ok.cc       | Taiwan        | TW   | Data Communication Business Group | 118.165.35.1                         | Yes (Region: TW) |

## Valid
```
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjg0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk0ODU5NjA1MzIxIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDIiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjg4IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk1OTkzMDcxMDI5IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDUiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNjcuMjEuOTAuNSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJwb3J0IjogNDQzLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzU0MDk4NTQueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDQyOTkwODc0OCIsICJ0bHMiOiAidGxzIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToyNzM5Y2U4NWQzYjllMTQ1@jscm01.celerlink.one:41020#github.com/freefq%20-%20%E6%B1%9F%E8%8B%8F%E7%9C%81%E7%9B%90%E5%9F%8E%E5%B8%82%E7%A7%BB%E5%8A%A8%207
vmess://eyJhZGQiOiAiNDZjYWFkYi5mMi5nbGFkbnMuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICI1N2UwY2I0ZC1lYWU1LTQ4ZWMtODA5MS0xNDlkYzJiMzA5ZTAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3MvNDZjYWFkYi5mbS5hcHBsZS5jb206NjA5ODAiLCAicG9ydCI6IDMzMzEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMShIaU5ldClcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxOCIsICJhZGQiOiAiNDUuMTk5LjEzOC4xNTIiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTQ2OTBkZDI0IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjMyNTIyMTc4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY1OTgwMTM4NTEiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAic25lZWQtYS52Mm9rLmNjIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICI0ODExZGJiOC0yZjliLTMyODktOGZhYy0wNWY2ZGFmN2NiMTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMjMwMDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMShIaU5ldClcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjAiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

