
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn             | cc   | isp                    | ip                        | chatgpt          |
|---:|:---------------------|:---------------|:---------------|:-----|:-----------------------|:--------------------------|:-----------------|
|  0 | [2](config/2.json)   | 45.58.186.81   | United States  | US   | SHARKTECH              | 64.32.2.26                | Yes (Region: US) |
|  1 | [3](config/3.json)   | 23.225.211.21  | United States  | US   | CNSERVERS              | 23.225.57.210             | Yes (Region: US) |
|  2 | [5](config/5.json)   | 45.199.138.121 | Netherlands    | NL   | YISP B.V.              | 46.182.107.129            | Yes (Region: US) |
|  3 | [6](config/6.json)   | 45.199.138.168 | Netherlands    | NL   | YISP B.V.              | 154.84.1.145              | Yes (Region: NL) |
|  4 | [8](config/8.json)   | 103.160.204.30 | Netherlands    | NL   | YISP B.V.              | 154.84.1.230              | Yes (Region: NL) |
|  5 | [13](config/13.json) | Shopify.com    | France         | FR   | CLOUDFLARENET          | 2a09:bac5:3264:be::13:298 | Yes (Region: FR) |
|  6 | [17](config/17.json) | vuk1.0bad.com  | United Kingdom | GB   | Akamai Connected Cloud | 178.79.144.65             | Yes (Region: GB) |
|  7 | [22](config/22.json) | 104.20.18.54   | United States  | US   | 24.hk global BGP       | 163.197.245.87            | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiNDUuNTguMTg2LjgxIiwgInBvcnQiOiAiNTExNDAiLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi9mb290ZXJzIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDZXJhTmV0d29ya3NcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMjMuMjI1LjIxMS4yMSIsICJwb3J0IjogIjQyOTQxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xMjEiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5NTQ5YTJjZi0xMjliLTQzYTEtODhkYi1lZjdmNjQ4ZGU3NGEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTEyMDQsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE2OCIsICJwb3J0IjogIjQ5NTU1IiwgImlkIjogIjZlNzllZWE0LTVmNzItNDY4My1hZDBlLTUzMzlmMDEzNDIxYiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZmFcdWQ4M2NcdWRkZjhVU1x1N2Y4ZVx1NTZmZCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTAzLjE2MC4yMDQuMzAiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZTlhXHU1OTJhXHU1NzMwXHU1MzNhICA4IiwgInBvcnQiOiA0NDMsICJpZCI6ICJhMjI4NGNjMS0yMGQ4LTRjNzgtYTYyMi0zZTNjY2E3NjdhNzAiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiZGVkaTIuMTgwOC5jZiIsICJwYXRoIjogImEyMjg0Y2MxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDEzIiwgImFkZCI6ICJTaG9waWZ5LmNvbSIsICJwb3J0IjogIjIwODYiLCAiaWQiOiAiMjUwZjQzMzEtOGMzZS00Yjg3LWE4NmItNWM1ZmJmOWRkYmE4IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJGci5jbG91ZGZsYXJlLnF1ZXN0IiwgInBhdGgiOiAiL2FyaWVzIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgyZjFcdTU2ZmRcdTRmMjZcdTY1NjZMaW5vZGVcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTciLCAiYWRkIjogInZ1azEuMGJhZC5jb20iLCAicG9ydCI6ICI0NDMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvY2hhdCIsICJob3N0IjogInZ1azEuMGJhZC5jb20iLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIyIiwgImFkZCI6ICIxMDQuMjAuMTguNTQiLCAicG9ydCI6ICIyMDk1IiwgImlkIjogIjhjNGU1ZTgzLThiZTItNDYzOC1lM2Y2LWEwOThlZTQ4NDE5MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiaGsud3loa2FhMC50ayIsICJwYXRoIjogIi9AaGthYTAiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

