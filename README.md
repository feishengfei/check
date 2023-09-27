
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp       | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:----------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 156.245.8.146  | Netherlands   | NL   | YISP B.V. | 154.84.1.134   | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 45.199.138.206 | Netherlands   | NL   | YISP B.V. | 154.84.1.129   | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.245.8.248  | Netherlands   | NL   | YISP B.V. | 154.84.1.137   | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 154.85.1.244   | Netherlands   | NL   | YISP B.V. | 154.84.1.206   | Yes (Region: NL) |
|  4 | [8](config/8.json)   | 64.32.24.222   | Poland        | PL   | OVH SAS   | 54.36.174.181  | Yes (Region: FR) |
|  5 | [10](config/10.json) | 156.225.67.48  | Netherlands   | NL   | YISP B.V. | 154.84.1.164   | Yes (Region: NL) |
|  6 | [13](config/13.json) | 107.167.16.85  | United States | US   | SHARKTECH | 170.178.189.50 | Yes (Region: US) |
|  7 | [14](config/14.json) | 45.199.138.180 | Netherlands   | NL   | YISP B.V. | 154.84.1.229   | Yes (Region: NL) |
|  8 | [17](config/17.json) | 154.85.1.204   | Netherlands   | NL   | YISP B.V. | 154.84.1.229   | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYzYjRiODI5LTdmMDEtNGUyNi1iMDM3LWYwNGIxZjA5ODc2NSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0Mjk1MiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgImFkZCI6ICI0NS4xOTkuMTM4LjIwNiIsICJwb3J0IjogIjQ0MDk0IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIyMGIzMDkxNi1lMjAzLTQxMmUtOGVjMC05MDBmM2FjZDUxMjgiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjI0OCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjk2NGJmNDk5LTllYzAtNDM3OC05MmI2LTg3ZDhkODYxYjJkMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MTY3MSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDU0OTgyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjIyIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiY2ZmOWQ4NjAtNzMzMC00ZWUxLWIwNzItNzE0MmRkZjE1NzFkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzA4MDgyMjI3MjkxNCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny40OCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjNjYTkxMmRhLTZhYzItNDE4Zi1iOWNmLTQ1YjZmNjk0NTc5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NTQ5MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICAxMCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAiYWRkIjogIjEwNy4xNjcuMTYuODUiLCAicG9ydCI6IDQ0MywgImlkIjogIjc2NDBhMWU3LTk3MDEtNDI4ZS1hNGIyLTE5YjNlN2RkNmY5ZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41MTEwOTA1Ny54eXoiLCAicGF0aCI6ICIvcGF0aC8wODA4MjIyNzI5MTQiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNCIsICJhZGQiOiAiNDUuMTk5LjEzOC4xODAiLCAicG9ydCI6ICI1NDg4NSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiZDMxMzM0ODQtZjJiZi00YjBjLThkMzgtZjhlNjQ1YjY1Njg3IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTciLCAiYWRkIjogIjE1NC44NS4xLjIwNCIsICJwb3J0IjogIjU0ODg1IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJkMzEzMzQ4NC1mMmJmLTRiMGMtOGQzOC1mOGU2NDViNjU2ODciLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvcGF0aC8xNjk1NTUyMzk3MzE4IiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
```

