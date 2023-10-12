
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp              | ip             | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:-----------------|:---------------|:-----------------|
|  0 | [1](config/1.json)   | 67.21.90.5       | United States | US   | SHARKTECH        | 107.167.22.10  | Yes (Region: US) |
|  1 | [4](config/4.json)   | 146.190.99.55    | Singapore     | SG   | DIGITALOCEAN-ASN | 146.190.99.55  | Yes (Region: SG) |
|  2 | [5](config/5.json)   | www.75409854.xyz | United States | US   | SHARKTECH        | 107.167.22.10  | Yes (Region: US) |
|  3 | [11](config/11.json) | 183.238.202.173  | Hong Kong     | HK   | CNSERVERS        | 156.227.19.218 | Yes (Region: US) |
|  4 | [18](config/18.json) | 45.199.138.222   | Netherlands   | NL   | YISP B.V.        | 154.84.1.122   | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiNjcuMjEuOTAuNSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMSIsICJwb3J0IjogNDQzLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzU0MDk4NTQueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDQyOTkwODc0OCIsICJ0bHMiOiAidGxzIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpMYW02bWdJMFpuSXFUNDU5Q1RUT0pS@us01.shawbrothersstudio.com:19922#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E7%A7%BB%E5%8A%A8%203
vmess://eyJhZGQiOiAiMTQ2LjE5MC45OS41NSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMDgxMzg2MmUtZWZmOS00NjY2LWNmNzAtMDBiZTgxZDVjYzdmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9TSEFMQU5BIiwgInBvcnQiOiAyMTcyNSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwb3J0IjogIjQ0MyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk0NDI5OTA4NzQ4IiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTEiLCAiYWRkIjogIjE4My4yMzguMjAyLjE3MyIsICJwb3J0IjogIjUxOTA0IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxOCIsICJhZGQiOiAiNDUuMTk5LjEzOC4yMjIiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjE5MjI5MzYyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTYyNTE2OTMwNDgiLCAidGxzIjogInRscyJ9
```

