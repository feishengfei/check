
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn          | cc   | isp                    | ip                | chatgpt          |
|---:|:---------------------|:---------------------|:------------|:-----|:-----------------------|:------------------|:-----------------|
|  0 | [4](config/4.json)   | 45.199.138.186       | Netherlands | NL   | YISP B.V.              | 154.84.1.122      | Yes (Region: NL) |
|  1 | [5](config/5.json)   | 156.225.67.104       | Netherlands | NL   | YISP B.V.              | 154.84.1.44       | Yes (Region: NL) |
|  2 | [11](config/11.json) | 198.41.217.5         | Netherlands | NL   | Aeza International Ltd | 2a12:5940:f1d9::2 | Yes (Region: NL) |
|  3 | [15](config/15.json) | gzcm01.celerlink.one | Singapore   | SG   | ORACLE-BMC-31898       | 158.178.226.110   | Yes (Region: SG) |
|  4 | [16](config/16.json) | 154.85.1.244         | Netherlands | NL   | YISP B.V.              | 154.84.1.216      | Yes (Region: NL) |
|  5 | [20](config/20.json) | 183.238.202.173      | Hong Kong   | HK   | CNSERVERS              | 156.227.19.218    | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4NiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NzM3Njc4Mjg3OSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY5NDQ4MDY5NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTk4LjQxLjIxNy41IiwgImFpZCI6ICIwIiwgImFscG4iOiAiaDIsaHR0cC8xLjEiLCAiZnAiOiAiY2hyb21lIiwgImhvc3QiOiAiZG9jczIub2JuZWgyNDcuaXIiLCAiaWQiOiAiOWM3ZGUzZTgtYzJhYS00ZmUwLWI2ODktOWIyNmQyMWU5Nzg2IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8ydjJyYXlURUFNIiwgInBvcnQiOiAiMjA4NyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTEiLCAic2N5IjogImF1dG8iLCAic25pIjogImRvY3MyLm9ibmVoMjQ3LmlyIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozNTI1NTg4ZWUxNGVhOTI0@gzcm01.celerlink.one:41040#github.com/freefq%20-%20%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%A7%BB%E5%8A%A8%2015
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTYiLCAiYWRkIjogIjE1NC44NS4xLjI0NCIsICJwb3J0IjogMzAwMDAsICJpZCI6ICIxZDQ3NGYwYi1lNzhkLTRhZjktYmM0YS1hNDY3NDY3YmM3YTciLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMjgxMTUzNjEueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5Njk0NDgwNjk2MSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMjAiLCAiYWRkIjogIjE4My4yMzguMjAyLjE3MyIsICJwb3J0IjogIjUxOTA0IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

