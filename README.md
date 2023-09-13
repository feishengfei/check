
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn             | cc   | isp               | ip             | chatgpt          |
|---:|:---------------------|:---------------|:---------------|:-----|:------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.204 |                |      |                   | 154.84.1.129   | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 156.225.67.95  | Netherlands    | NL   | YISP B.V.         | 154.84.1.40    | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 172.99.190.12  | United Kingdom | GB   | AS-GLOBALTELEHOST | 172.99.190.12  | Yes (Region: GB) |
|  3 | [5](config/5.json)   | 45.58.179.155  | United States  | US   | SHARKTECH         | 107.167.18.50  | Yes (Region: US) |
|  4 | [8](config/8.json)   | 57.128.173.208 |                |      |                   | 54.36.174.181  | Yes (Region: FR) |
|  5 | [14](config/14.json) | 162.159.60.89  | Spain          | ES   | NIXVAL            | 213.162.210.42 | Yes (Region: ES) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4yMDQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIyMGIzMDkxNi1lMjAzLTQxMmUtOGVjMC05MDBmM2FjZDUxMjgiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTExOTQsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny45NSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjVhNGQ2OWFkLTIwYTktNDk0MS1iMjIzLTg3YmJkMDlmNWY1MiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1MzM4MSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTcyLjk5LjE5MC4xMiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMDQ2MjFiYWUtYWIzNi0xMWVjLWI5MDktMDI0MmFjMTIwMDAyIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDIyMzI0LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiNDUuNTguMTc5LjE1NSIsICJwb3J0IjogNDQzLCAiaWQiOiAiYmRlZTIwMmMtOGZhZS00NDFmLWE1ODgtN2JjNGQzODg3MDE5IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjQwMTU0NTc3Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZjZDVcdTU2ZmRcdTU2ZmRcdTk2NDVcdTgyMmFcdTdhN2FcdTc1MzVcdThiYWZcdTk2YzZcdTU2ZTJcdTUxNmNcdTUzZjgoU0lUQSkgOCIsICJhZGQiOiAiNTcuMTI4LjE3My4yMDgiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI0ZTY2ZTdkNi1iYWIwLTQwM2QtOGFiMi02Mzk3MDkwZDM2MTIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInVrMi12bWVzcy5ncmVlbnNzaC54eXoiLCAicGF0aCI6ICIvdm1lc3MiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE0IiwgImFkZCI6ICIxNjIuMTU5LjYwLjg5IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiN2E2MGMxNWUtY2JjZC00ODZkLWFlZTYtMDdhNDk0ZjQwM2UzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ4YnkuZGFvemhhbmcubGluayIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
```

