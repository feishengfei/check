
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                    | ip              | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 192.74.228.161  | United States | US   | PEGTECHINC             | 142.0.129.201   | Yes (Region: US) |
|  1 | [3](config/3.json)   | 156.225.67.159  | Netherlands   | NL   | YISP B.V.              | 154.84.1.197    | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 45.199.138.132  | Netherlands   | NL   | YISP B.V.              | 154.84.1.206    | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 156.245.8.158   | Netherlands   | NL   | YISP B.V.              | 154.84.1.138    | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 156.245.8.129   | Netherlands   | NL   | YISP B.V.              | 154.84.1.164    | Yes (Region: NL) |
|  5 | [8](config/8.json)   | 137.175.1.13    | United States | US   | CNSERVERS              | 23.225.9.234    | Yes (Region: US) |
|  6 | [17](config/17.json) | 142.4.99.90     | United States | US   | PEGTECHINC             | 142.4.99.65     | Yes (Region: US) |
|  7 | [19](config/19.json) | 172.104.131.215 | Germany       | DE   | Akamai Connected Cloud | 172.104.131.215 | Yes (Region: DE) |

## Valid
```
vmess://eyJhZGQiOiAiMTkyLjc0LjIyOC4xNjEiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDI4NTcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNTkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5YzAyNmVmZS02YWYwLTQ2NWYtYjhjMC0zZjU4YzhjMmQ0YzUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDg5MjEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xMzIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIxZDQ3NGYwYi1lNzhkLTRhZjktYmM0YS1hNDY3NDY3YmM3YTciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTU1OTUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE1OCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDUiLCAicG9ydCI6IDQ4MTIzLCAiaWQiOiAiMTExMTdkNGMtM2I2YS00ZTc2LThiY2MtMmI0MWIzZTljYTkzIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDYiLCAiYWRkIjogIjE1Ni4yNDUuOC4xMjkiLCAicG9ydCI6ICI0ODEyMyIsICJpZCI6ICIzY2E5MTJkYS02YWMyLTQxOGYtYjljZi00NWI2ZjY5NDU3OWIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDgiLCAiYWRkIjogIjEzNy4xNzUuMS4xMyIsICJwb3J0IjogIjUzNDAzIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTQyLjQuOTkuOTAiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0ggMTciLCAicG9ydCI6IDQzMzc5LCAiaWQiOiAiYjY1ZGE0YWYtYTEyYS00YTU5LTkzMTYtNDU0OWUxMmJhNjJjIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozMzQ0MTA0NjU3@172.104.131.215:42951#github.com/freefq%20-%20%E5%BE%B7%E5%9B%BD%E9%BB%91%E6%A3%AE%E5%B7%9E%E6%B3%95%E5%85%B0%E5%85%8B%E7%A6%8FLinode%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2019
```

