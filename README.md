
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn            | cc   | isp                    | ip                                  | chatgpt          |
|---:|:---------------------|:----------------------------|:--------------|:-----|:-----------------------|:------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 156.225.67.104              | Netherlands   | NL   | YISP B.V.              | 154.84.1.44                         | Yes (Region: NL) |
|  1 | [6](config/6.json)   | 146.190.110.92              | Singapore     | SG   | DIGITALOCEAN-ASN       | 146.190.110.92                      | Yes (Region: SG) |
|  2 | [7](config/7.json)   | 45.199.138.191              | Netherlands   | NL   | YISP B.V.              | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba | Yes (Region: NL) |
|  3 | [9](config/9.json)   | 45.199.138.186              | Netherlands   | NL   | YISP B.V.              | 154.84.1.122                        | Yes (Region: NL) |
|  4 | [10](config/10.json) | us02.shawbrothersstudio.com | United States | US   | NETLAB-SDN             | 154.40.56.206                       | Yes (Region: US) |
|  5 | [12](config/12.json) | 45.199.138.222              | Netherlands   | NL   | YISP B.V.              | 154.84.1.122                        | Yes (Region: NL) |
|  6 | [13](config/13.json) | 120.233.43.41               | Singapore     | SG   | Akamai Connected Cloud | 170.187.229.119                     | Yes (Region: SG) |
|  7 | [14](config/14.json) | 120.233.43.31               | Singapore     | SG   | Akamai Connected Cloud | 170.187.229.119                     | Yes (Region: SG) |
|  8 | [17](config/17.json) | api.jquery.com              | Netherlands   | NL   | AS-GLOBALTELEHOST      | 172.99.190.170                      | Yes (Region: GB) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY5NDQ4MDY5NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDYiLCAiYWRkIjogIjE0Ni4xOTAuMTEwLjkyIiwgInBvcnQiOiAyMjExOCwgImlkIjogImI4MDBmYmE2LTI4MzUtNGI0NC04M2MyLTUyNzVmZGJiMjRiYSIsICJhaWQiOiAwLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIm1lZGlhLWV4cDEubGljZG4uY29tIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAibm9uZSJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTEiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy40MjA3NzIzMC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTYyNTE1MjI0MzgiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA3IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xODYiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTY1OTgwMTM4NTEiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA5IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpoZzloNUtwTW1KTGxpNlc2UWpkMnlp@us02.shawbrothersstudio.com:43642#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E6%96%B0%E5%9B%BD%E4%BF%A1%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2010
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMiIsICJhZGQiOiAiNDUuMTk5LjEzOC4yMjIiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NjI1MTY5MzA0OCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTIwLjIzMy40My40MSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiZDQwZDk3NmQtZDU2OS0zZTdkLTkzOTYtMTMyZGVhNjBjZjI4IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDI2MDIzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTIwLjIzMy40My4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiZDQwZDk3NmQtZDU2OS0zZTdkLTkzOTYtMTMyZGVhNjBjZjI4IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDI2MDIxLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE3IiwgImFkZCI6ICJhcGkuanF1ZXJ5LmNvbSIsICJwb3J0IjogNDQzLCAiaWQiOiAiMDNmY2M2MTgtYjkzZC02Nzk2LTZhZWQtOGEzOGM5NzVkNTgxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJzdWIueWlmZW5qaWNoYW5nLnRvcCIsICJwYXRoIjogIi9vbGl2LmJlYXV0eTo0NDMvbGlua3Z3cyIsICJ0bHMiOiAidGxzIn0=
```

