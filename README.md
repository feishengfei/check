
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp                                      | ip                        | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:-----------------------------------------|:--------------------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.126.24     | China         | CN   | PEG-SV                                   | 142.4.126.17              | Yes (Region: US) |
|  1 | [3](config/3.json)   | 45.199.138.176   | United States | US   | NovoServe B.V.                           | 45.199.138.43             | Yes (Region: US) |
|  2 | [5](config/5.json)   | scw-fr.iiio.wiki | France        | FR   | CLOUDFLARENET                            | 2a09:bac5:3264:be::13:288 | Yes (Region: FR) |
|  3 | [6](config/6.json)   | 64.32.21.241     | United States | US   | SHARKTECH                                | 107.167.24.162            | Yes (Region: US) |
|  4 | [8](config/8.json)   | 104.18.236.126   | Poland        | PL   | OVH SAS                                  | 54.36.174.181             | Yes (Region: FR) |
|  5 | [20](config/20.json) | 13.wyhkaa0.gq    | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 45.137.97.241             | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAyIiwgImFkZCI6ICIxNDIuNC4xMjYuMjQiLCAicG9ydCI6ICI1MTcxNSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiIsICJmcCI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNzYiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI2ZmE1NjBkNC0zNWM1LTQ5NjgtYWRmYy04MTJjNTI4NzhiODQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQ5ODUyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAic2N3LWZyLmlpaW8ud2lraSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMjUwZjQzMzEtOGMzZS00Yjg3LWE4NmItNWM1ZmJmOWRkYmE4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInBvcnQiOiAyMDgyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuMjEuMjQxIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2IiwgInBvcnQiOiA0NDMxMywgImlkIjogIjU3ZjkzZTkyLWViYjktNGYxNi05YmRjLTgyMjVkMjAxMDk5NSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi9xd2VyIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTA0LjE4LjIzNi4xMjYiLCAiYWlkIjogMCwgImhvc3QiOiAiZWNjLnZ0Y3NzLnRvcCIsICJpZCI6ICI3NGE4OTBhYi01YzRiLTRmMzUtYWVhNC01ZmMyNDU5YmViZDIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2JsdWUiLCAicG9ydCI6IDgwODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIwIiwgImFkZCI6ICIxMy53eWhrYWEwLmdxIiwgInBvcnQiOiAyMDk1LCAiaWQiOiAiMzJhZjQwMDYtMDY5OC00OTEwLTgwNmMtYjgxMzA3NGYzNmViIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICIxMy53eWhrYWEwLmdxIiwgInBhdGgiOiAiL1RHOkBoa2FhMCIsICJ0bHMiOiAiIn0=
```

