
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn             | cc   | isp               | ip             | chatgpt          |
|---:|:---------------------|:----------------|:---------------|:-----|:------------------|:---------------|:-----------------|
|  0 | [4](config/4.json)   | 172.99.190.12   | United Kingdom | GB   | AS-GLOBALTELEHOST | 172.99.190.12  | Yes (Region: GB) |
|  1 | [5](config/5.json)   | 142.4.99.85     | China          | CN   | PEG-SV            | 142.4.99.65    | Yes (Region: US) |
|  2 | [6](config/6.json)   | 156.245.8.142   | Netherlands    | NL   | YISP B.V.         | 154.84.1.139   | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 156.225.67.229  | Netherlands    | NL   | YISP B.V.         | 154.84.1.219   | Yes (Region: NL) |
|  4 | [8](config/8.json)   | 156.245.8.248   | Netherlands    | NL   | YISP B.V.         | 154.84.1.137   | Yes (Region: NL) |
|  5 | [9](config/9.json)   | 156.225.67.71   | Netherlands    | NL   | YISP B.V.         | 154.84.1.19    | Yes (Region: NL) |
|  6 | [11](config/11.json) | 156.245.8.130   | Netherlands    | NL   | YISP B.V.         | 154.84.1.121   | Yes (Region: NL) |
|  7 | [12](config/12.json) | 45.199.138.205  | Netherlands    | NL   | YISP B.V.         | 154.84.1.129   | Yes (Region: NL) |
|  8 | [13](config/13.json) | 154.85.1.244    | Netherlands    | NL   | YISP B.V.         | 154.84.1.216   | Yes (Region: NL) |
|  9 | [14](config/14.json) | 156.225.67.104  | Netherlands    | NL   | YISP B.V.         | 154.84.1.44    | Yes (Region: NL) |
| 10 | [17](config/17.json) | 107.167.16.85   | United States  | US   | SHARKTECH         | 170.178.189.50 | Yes (Region: US) |
| 11 | [20](config/20.json) | 183.238.202.173 | Hong Kong      | HK   | CNSERVERS         | 156.227.19.218 | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTcyLjk5LjE5MC4xMiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMDQ2MjFiYWUtYWIzNi0xMWVjLWI5MDktMDI0MmFjMTIwMDAyIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDIyMzI0LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA1IiwgImFkZCI6ICIxNDIuNC45OS44NSIsICJwb3J0IjogNDQzLCAiaWQiOiAiYjY1ZGE0YWYtYTEyYS00YTU5LTkzMTYtNDU0OWUxMmJhNjJjIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjczMzMyNDYzLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTcyODg3MjIyNjYiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDYiLCAiYWRkIjogIjE1Ni4yNDUuOC4xNDIiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNjE5MzExNmQtOTZmOS00ZDdhLTliZTUtNWJiMDZhNjlhZjBiIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjkyODczODg5Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTcyODg3MjIyNjYiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDciLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjI5IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjUxNWJjYjRkLTBiYTEtNGNhZS04N2NmLWEwNDcwMDdlZWM1NCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy43MzkzODAyMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk3Mzc2NzgyODc5IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDgiLCAiYWRkIjogIjE1Ni4yNDUuOC4yNDgiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiOTY0YmY0OTktOWVjMC00Mzc4LTkyYjYtODdkOGQ4NjFiMmQwIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjgxNjc4MDM0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTcyODg3MjIyNjYiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDkiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzEiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiMjExNTVlZmQtOGUyOS00M2QyLTk1YmMtZmUzMTkwZWNiMWM2IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjE1MDU5NzgyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTczNzY3ODI4NzkiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDExIiwgImFkZCI6ICIxNTYuMjQ1LjguMTMwIiwgInBvcnQiOiAzMDAwMCwgImlkIjogImJkMjQ5ZTM3LTczNTktNDFlZS04NGE3LTA5ZTQ5ZTBlYzVjNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy40NzUyMzM3NS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk3Mzc2NzgyODc5IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMiIsICJhZGQiOiAiNDUuMTk5LjEzOC4yMDUiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiMjBiMzA5MTYtZTIwMy00MTJlLThlYzAtOTAwZjNhY2Q1MTI4IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjY5NzA4MjcyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTczNzY3ODI4NzkiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAiYWRkIjogIjE1NC44NS4xLjI0NCIsICJwb3J0IjogMzAwMDAsICJpZCI6ICIxZDQ3NGYwYi1lNzhkLTRhZjktYmM0YS1hNDY3NDY3YmM3YTciLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMjgxMTUzNjEueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5Njk0NDgwNjk2MSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE0IiwgImFkZCI6ICIxNTYuMjI1LjY3LjEwNCIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy40MTc1ODExMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTciLCAiYWRkIjogIjEwNy4xNjcuMTYuODUiLCAicG9ydCI6IDQ0MywgImlkIjogIjc2NDBhMWU3LTk3MDEtNDI4ZS1hNGIyLTE5YjNlN2RkNmY5ZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41MTEwOTA1Ny54eXoiLCAicGF0aCI6ICIvcGF0aC8wODA4MjIyNzI5MTQiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMjAiLCAiYWRkIjogIjE4My4yMzguMjAyLjE3MyIsICJwb3J0IjogIjUxOTA0IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

