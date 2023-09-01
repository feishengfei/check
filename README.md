
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp                                      | ip             | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:-----------------------------------------|:---------------|:-----------------|
|  0 | [1](config/1.json)   | 142.4.111.76         | China         | CN   | PEG-SV                                   | 142.4.111.65   | Yes (Region: US) |
|  1 | [2](config/2.json)   | 64.32.4.53           | United States | US   | SHARKTECH                                | 107.167.13.162 | Yes (Region: US) |
|  2 | [4](config/4.json)   | 45.199.138.157       | Netherlands   | NL   | YISP B.V.                                | 154.84.1.231   | Yes (Region: NL) |
|  3 | [8](config/8.json)   | cfcdn2.sanfencdn.net | Poland        | PL   | OVH SAS                                  | 54.36.174.181  | Yes (Region: FR) |
|  4 | [23](config/23.json) | 11.wyhkaa0.gq        | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 45.137.97.230  | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTQyLjQuMTExLjc2IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQyMDAyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAxIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuNC41MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MzU1NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmt0ZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNTciLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmNTI1MGM0ZS1mODU1LTRlZmYtYjczYy1hMDIyMjZkNDJmZTciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk3NzQsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiY2ZjZG4yLnNhbmZlbmNkbi5uZXQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA4IiwgInBvcnQiOiA0NDMsICJpZCI6ICI0ODg0MzIzMi01OGU3LTQyOWYtOTBmYi0zODA5MDc0Y2MwYmIiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAidXM0LnNhbmZlbmNkbjEuY29tIiwgInBhdGgiOiAiL3poLWNuIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTEud3loa2FhMC5ncSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIzIiwgInBvcnQiOiAyMDk1LCAiaWQiOiAiYTU0ZmQzYmMtMzc2NC00MGNkLWZmNWEtNDcxNDcwNDE3ZWFjIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogIjExLnd5aGthYTAuZ3EiLCAicGF0aCI6ICIvVEc6QGhrYWEwIiwgInRscyI6ICIifQ==
```

