
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp       | ip                                   | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:----------|:-------------------------------------|:-----------------|
|  0 | [6](config/6.json)   | 45.58.152.70        | Netherlands   | NL   | SHARKTECH | 2610:150:4000:1da:225:90ff:fea7:7db4 | Yes (Region: US) |
|  1 | [9](config/9.json)   | 183.233.187.214     | China         | CN   | CNSERVERS | 192.151.223.154                      | Yes (Region: US) |
|  2 | [10](config/10.json) | bjcu.xzyunjiasu.icu | United States | US   | PONYNET   | 209.141.58.10                        | Yes (Region: US) |
|  3 | [11](config/11.json) | 45.199.138.191      | Netherlands   | NL   | YISP B.V. | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba  | Yes (Region: NL) |
|  4 | [15](config/15.json) | 45.199.138.146      | Netherlands   | NL   | YISP B.V. | 154.84.1.122                         | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiNDUuNTguMTUyLjcwIiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41NDk2NDc0NS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5MTkzMTAwMzg4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvNWYyZWE1MzEtMjllNC00ODM2LWM2MGEtYTczOWI4ZTZiMGEzIiwgInBvcnQiOiA1NjI2NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1ZTdmXHU0ZTFjXHU3NzAxXHU1ZTdmXHU1ZGRlXHU1ZTAyXHU3OWZiXHU1MmE4IDkiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICJraW5nLnR1cmJvMDIxLmxpbmsifQ==
ss://YWVzLTI1Ni1nY206NWM4YjIxMGEtMmYwMC00MjkyLTk2NGItMDUyODFjN2FkNWQx@bjcu.xzyunjiasu.icu:33952#github.com/freefq%20-%20%E6%B9%96%E5%8D%97%E7%9C%81%E8%81%94%E9%80%9A%2010
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMSIsICJhZGQiOiAiNDUuMTk5LjEzOC4xOTEiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjQyMDc3MjMwLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkyODAwOTkxMzgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNSIsICJhZGQiOiAiNDUuMTk5LjEzOC4xNDYiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjE5MjI5MzYyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkxOTMxMDAzODgiLCAidGxzIjogInRscyJ9
```

