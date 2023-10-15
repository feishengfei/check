
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                               | ip             | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:----------------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 107.167.16.85   | United States | US   | SHARKTECH                         | 170.178.189.50 | Yes (Region: US) |
|  1 | [4](config/4.json)   | 154.85.1.244    | Netherlands   | NL   | YISP B.V.                         | 154.84.1.216   | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 156.225.67.104  | Netherlands   | NL   | YISP B.V.                         | 154.84.1.44    | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 146.190.96.141  | Singapore     | SG   | DIGITALOCEAN-ASN                  | 146.190.96.141 | Yes (Region: SG) |
|  4 | [8](config/8.json)   | b.baozinet.top  | Taiwan        | TW   | Data Communication Business Group | 36.231.161.220 | Yes (Region: TW) |
|  5 | [12](config/12.json) | 183.238.202.173 | Hong Kong     | HK   | CNSERVERS                         | 156.227.19.218 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTA3LjE2Ny4xNi44NSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNzY0MGExZTctOTcwMS00MjhlLWE0YjItMTliM2U3ZGQ2ZjlmIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjUxMTA5MDU3Lnh5eiIsICJwYXRoIjogIi9wYXRoLzA4MDgyMjI3MjkxNCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODExNTM2MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY5NDQ4MDY5NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTQ2LjE5MC45Ni4xNDEiLCAiYWlkIjogMCwgImhvc3QiOiAibWVkaWEtZXhwMS5saWNkbi5jb20iLCAiaWQiOiAiY2RiY2EyNjYtMTBkOS00MDE4LWU5OWUtYzU2MTQ5N2Q2NTQyIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9pc3VydSIsICJwb3J0IjogNTU1OTksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgNyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggOCIsICJhZGQiOiAiYi5iYW96aW5ldC50b3AiLCAicG9ydCI6ICIyNTAxMCIsICJpZCI6ICI1MGI0NzllNi04ODhkLTQyYmItYjBkZC0wZWE5OTM1ZjdhN2UiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogIjE4My4yMzguMjAyLjE3MyIsICJwb3J0IjogIjUxOTA0IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

