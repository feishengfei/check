
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                 | ip             | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:--------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.173           | Netherlands   | NL   | YISP B.V.           | 154.84.1.129   | Yes (Region: NL) |
|  1 | [8](config/8.json)   | 45.76.147.196            | Poland        | PL   | OVH SAS             | 54.36.174.181  | Yes (Region: FR) |
|  2 | [14](config/14.json) | 156.225.67.38            | Netherlands   | NL   | YISP B.V.           | 154.84.1.16    | Yes (Region: NL) |
|  3 | [21](config/21.json) | vmesskhodammtn1.ddns.net | Germany       | DE   | Hetzner Online GmbH | 91.107.241.210 | Yes (Region: DE) |
|  4 | [33](config/33.json) | 20.kccic2pa.xyz          | United States | US   | SERVERSTADIUM       | 74.121.188.130 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAyIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE3MyIsICJwb3J0IjogIjQ3MTU0IiwgImlkIjogIjIwYjMwOTE2LWUyMDMtNDEyZS04ZWMwLTkwMGYzYWNkNTEyOCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1YjBcdTUyYTBcdTU3NjFDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJhZGQiOiAiNDUuNzYuMTQ3LjE5NiIsICJwb3J0IjogIjEwMDAwIiwgImlkIjogIjlhODZhNTBhLTNjZjgtMTFlZS1hNGEzLWM3NmYwMjY5NjJkMSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiNDUuNzYuMTQ3LjE5NiIsICJwYXRoIjogIi92cG5qYW50aXQiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE0IiwgImFkZCI6ICIxNTYuMjI1LjY3LjM4IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImRlNDkxODAyLTIzM2UtNDdmMi04YzZjLWQxOWJjZjViZDU2YiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy44NjEzOTMxNy54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjkyMjU2OTAyNDMwIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTg5N2ZcdTczZWRcdTcyNTkgIDIxIiwgImFkZCI6ICJ2bWVzc2tob2RhbW10bjEuZGRucy5uZXQiLCAicG9ydCI6ICIyMDUzIiwgImlkIjogIjA0ZGViYTA3LWZiMTEtNDhlZC1lZjBjLWVlMjQxMDlkZTM0ZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidm1lc3NraG9kYW0udm1lc3NraG9kYW0udG9wIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTZkZjFcdTU3MzNcdTVlMDJcdTc5ZmJcdTUyYTggMzMiLCAiYWRkIjogIjIwLmtjY2ljMnBhLnh5eiIsICJwb3J0IjogIjUwMDIwIiwgImlkIjogImQ2YjVhNDM4LWQ3YTYtNGYzZS1hMWQ4LWUzMTMzOTJlMDA5OCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
```

