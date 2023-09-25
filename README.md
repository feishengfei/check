
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                           | cn            | cc   | isp                               | ip                  | chatgpt          |
|---:|:---------------------|:-------------------------------|:--------------|:-----|:----------------------------------|:--------------------|:-----------------|
|  0 | [3](config/3.json)   | 45.199.138.180                 | Netherlands   | NL   | YISP B.V.                         | 154.84.1.229        | Yes (Region: NL) |
|  1 | [5](config/5.json)   | sneed-a.v2ok.cc                | Taiwan        | TW   | Data Communication Business Group | 1.164.147.203       | Yes (Region: TW) |
|  2 | [6](config/6.json)   | 156.245.8.146                  | Netherlands   | NL   | YISP B.V.                         | 154.84.1.134        | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 107.167.16.85                  | United States | US   | SHARKTECH                         | 170.178.189.50      | Yes (Region: US) |
|  4 | [8](config/8.json)   | 154.85.1.244                   | Poland        | PL   | OVH SAS                           | 54.36.174.181       | Yes (Region: FR) |
|  5 | [20](config/20.json) | vxyfa-1080-v2-2.d-kcd.tuil.xyz | Japan         | JP   | Eons Data Communications Limited  | 2404:c140:221:4c::a | Yes (Region: JP) |
|  6 | [22](config/22.json) | 1.164.147.203                  | Taiwan        | TW   | Data Communication Business Group | 1.164.147.203       | Yes (Region: TW) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4MCIsICJwb3J0IjogIjU0ODg1IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJkMzEzMzQ4NC1mMmJmLTRiMGMtOGQzOC1mOGU2NDViNjU2ODciLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAic25lZWQtYS52Mm9rLmNjIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICI0OTBkOWZlYi1kNjc5LTNhZDEtYTM1OC03ZWJkZjA5ZTMwYTEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMjMwMDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NTNmMFx1NTMxN1x1NWUwMlx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYzYjRiODI5LTdmMDEtNGUyNi1iMDM3LWYwNGIxZjA5ODc2NSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0Mjk1MiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiMTA3LjE2Ny4xNi44NSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNzY0MGExZTctOTcwMS00MjhlLWE0YjItMTliM2U3ZGQ2ZjlmIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjUxMTA5MDU3Lnh5eiIsICJwYXRoIjogIi9wYXRoLzA4MDgyMjI3MjkxNCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDU0OTgyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTZkZjFcdTU3MzNcdTVlMDJcdTc5ZmJcdTUyYTggMjAiLCAiYWRkIjogInZ4eWZhLTEwODAtdjItMi5kLWtjZC50dWlsLnh5eiIsICJwb3J0IjogIjM5OTI4IiwgImlkIjogImE1OTBlNjkyLTRjOGQtNDJkZC1iYTgwLWIxNzY1YTM0ZjY5OSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZWRnZS5jamhoLm1vbSIsICJwYXRoIjogIi9qZTV4M3BCTjF2ZXozTlF1ZE5rQiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTUzZjBcdTUzMTdcdTVlMDJcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgMjIiLCAiYWRkIjogIjEuMTY0LjE0Ny4yMDMiLCAicG9ydCI6ICIyMzAwMCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDkwZDlmZWItZDY3OS0zYWQxLWEzNTgtN2ViZGYwOWUzMGExIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvP2VkPTIwNDgiLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
```

