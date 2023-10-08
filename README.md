
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn          | cc   | isp                               | ip                                   | chatgpt          |
|---:|:---------------------|:-----------------------|:------------|:-----|:----------------------------------|:-------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | sneed-a.v2ok.cc        | Taiwan      | TW   | Data Communication Business Group | 118.165.35.1                         | Yes (Region: TW) |
|  1 | [4](config/4.json)   | twpaopao.gfwisbest.xyz | Taiwan      | TW   | Data Communication Business Group | 36.227.193.110                       | Yes (Region: TW) |
|  2 | [8](config/8.json)   | 38.63.0.80             | Poland      | PL   | OVH SAS                           | 54.36.174.181                        | Yes (Region: FR) |
|  3 | [12](config/12.json) | 198.2.202.88           | China       | CN   | PEG-SV                            | 142.4.102.244                        | Yes (Region: US) |
|  4 | [18](config/18.json) | 45.199.138.222         | Netherlands | NL   | YISP B.V.                         | 154.84.1.122                         | Yes (Region: NL) |
|  5 | [20](config/20.json) | 45.199.138.152         | Netherlands | NL   | YISP B.V.                         | 2a02:2a38:1:2796:ae1f:6bff:fe24:8940 | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAic25lZWQtYS52Mm9rLmNjIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICI0ODExZGJiOC0yZjliLTMyODktOGZhYy0wNWY2ZGFmN2NiMTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMjMwMDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMShIaU5ldClcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAidHdwYW9wYW8uZ2Z3aXNiZXN0Lnh5eiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNDgxMWRiYjgtMmY5Yi0zMjg5LThmYWMtMDVmNmRhZjdjYjE5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDYwOTgyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTY1YjBcdTUzMTdcdTVlMDJcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggOCIsICJhZGQiOiAiMzguNjMuMC44MCIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTk0NTgxNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NjU5ODAxMzg1MSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTk4LjIuMjAyLjg4IiwgImFpZCI6IDY0LCAiaG9zdCI6ICJ3d3cuNjU4MjU1MjQueHl6IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk1OTkzMDcxMDI5IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlBldGFFeHByZXNzIDEyIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxOCIsICJhZGQiOiAiNDUuMTk5LjEzOC4yMjIiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NjI1MTY5MzA0OCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAyMCIsICJhZGQiOiAiNDUuMTk5LjEzOC4xNTIiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTQ2OTBkZDI0IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjMyNTIyMTc4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY1OTgwMTM4NTEiLCAidGxzIjogInRscyJ9
```

