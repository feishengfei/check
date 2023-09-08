
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                                        | ip                    | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-------------------------------------------|:----------------------|:-----------------|
|  0 | [4](config/4.json)   | 45.199.138.188  | Netherlands   | NL   | YISP B.V.                                  | 154.84.1.122          | Yes (Region: NL) |
|  1 | [5](config/5.json)   | 45.199.138.161  | Netherlands   | NL   | YISP B.V.                                  | 46.182.107.129        | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 04.kccic2pa.xyz | United States | US   | OVH SAS                                    | 15.204.10.95          | Yes (Region: US) |
|  3 | [8](config/8.json)   | 146.190.137.55  | Poland        | PL   | OVH SAS                                    | 54.36.174.181         | Yes (Region: FR) |
|  4 | [9](config/9.json)   | 07.kccic2pa.xyz | Austria       | AT   | Hohl IT e.U.                               | 2a0d:f302:109:1cbe::1 | Yes (Region: AT) |
|  5 | [16](config/16.json) | 45.199.138.173  | Netherlands   | NL   | YISP B.V.                                  | 154.84.1.129          | Yes (Region: NL) |
|  6 | [18](config/18.json) | 109.248.18.208  | Philippines   | PH   | HONG KONG Megalayer Technology Co.,Limited | 109.248.18.208        | Yes (Region: PH) |
|  7 | [23](config/23.json) | 46.182.107.22   | Netherlands   | NL   | YISP B.V.                                  | 154.84.1.16           | Yes (Region: NL) |
|  8 | [28](config/28.json) | 172.64.153.211  | Sweden        | SE   | Stark Industries Solutions Ltd             | 94.131.115.68         | Yes (Region: SE) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xODgiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzAwMDksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjEiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5NTQ5YTJjZi0xMjliLTQzYTEtODhkYi1lZjdmNjQ4ZGU3NGEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDg0NTMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggNiIsICJhZGQiOiAiMDQua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwMDQiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjEyMGNhZGYyLWUyNTQtNDA2OS05N2IyLWFjZDMzY2ZjNGYzZiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIjA0LmtjY2ljMnBhLnh5eiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDgiLCAiYWRkIjogIjE0Ni4xOTAuMTM3LjU1IiwgInBvcnQiOiAiMSIsICJpZCI6ICIxMDBmYjI5NC05OWZiLTRiNzEtZGIyOC0yMGNiMDIwODIwOTgiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIm0ubGljZG4uY29tIiwgInBhdGgiOiAiL3dpc2h2YSIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggOSIsICJhZGQiOiAiMDcua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwMDciLCAidHlwZSI6ICJub25lIiwgImlkIjogIjEyMGNhZGYyLWUyNTQtNDA2OS05N2IyLWFjZDMzY2ZjNGYzZiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogInNncGNvbnRhYm8uZG91YmxlZG91LmljdSIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNiIsICJhZGQiOiAiNDUuMTk5LjEzOC4xNzMiLCAicG9ydCI6ICI1Mjg5NCIsICJpZCI6ICIyMGIzMDkxNi1lMjAzLTQxMmUtOGVjMC05MDBmM2FjZDUxMjgiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmYzRcdTdmNTdcdTY1YWYgIDE4IiwgImFkZCI6ICIxMDkuMjQ4LjE4LjIwOCIsICJwb3J0IjogIjI1MDY1IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJjMGRlN2Q4ZC1iNDUyLTRhZWUtYzE1Ny03NmJjM2Y1MDk1NmQiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BobGl2ZXRlc3QiLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNDYuMTgyLjEwNy4yMiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImRlNDkxODAyLTIzM2UtNDdmMi04YzZjLWQxOWJjZjViZDU2YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzNjg1NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4Mzc3XHU1MTcwICAyMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI4IiwgImFkZCI6ICIxNzIuNjQuMTUzLjIxMSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJzY2hlcmVzd2VkLnNvZnR3YXJlbmV3cy5zdG9yZSIsICJwYXRoIjogIi9hcGkwMSIsICJ0bHMiOiAidGxzIn0=
```

