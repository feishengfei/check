
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn            | cc   | isp                    | ip                                  | chatgpt          |
|---:|:---------------------|:----------------------------|:--------------|:-----|:-----------------------|:------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 120.233.43.41               | Singapore     | SG   | Akamai Connected Cloud | 170.187.229.119                     | Yes (Region: SG) |
|  1 | [3](config/3.json)   | 104.17.27.2                 | United States | US   | Hetzner Online GmbH    | 5.161.199.86                        | Yes (Region: US) |
|  2 | [4](config/4.json)   | 154.85.1.244                | Netherlands   | NL   | YISP B.V.              | 154.84.1.216                        | Yes (Region: NL) |
|  3 | [6](config/6.json)   | 45.199.138.186              | Netherlands   | NL   | YISP B.V.              | 154.84.1.122                        | Yes (Region: NL) |
|  4 | [7](config/7.json)   | 45.199.138.222              | Netherlands   | NL   | YISP B.V.              | 154.84.1.122                        | Yes (Region: NL) |
|  5 | [9](config/9.json)   | 156.225.67.104              | Netherlands   | NL   | YISP B.V.              | 154.84.1.44                         | Yes (Region: NL) |
|  6 | [10](config/10.json) | 45.199.138.191              | Netherlands   | NL   | YISP B.V.              | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba | Yes (Region: NL) |
|  7 | [11](config/11.json) | 146.190.110.92              | Singapore     | SG   | DIGITALOCEAN-ASN       | 146.190.110.92                      | Yes (Region: SG) |
|  8 | [13](config/13.json) | www.75409854.xyz            | United States | US   | SHARKTECH              | 107.167.22.10                       | Yes (Region: US) |
|  9 | [16](config/16.json) | us02.shawbrothersstudio.com | United States | US   | NETLAB-SDN             | 154.40.56.206                       | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTIwLjIzMy40My40MSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiZDQwZDk3NmQtZDU2OS0zZTdkLTkzOTYtMTMyZGVhNjBjZjI4IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDI2MDIzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTA0LjE3LjI3LjIiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAibXkyLmdhbWVkYXlsaW9uLmJ1enoiLCAiaWQiOiAiNzJkNDYxNTItZWUwYi00NjEwLWVmYjEtZmZiMGY3ODZiODQ4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8_ZWQ9MjA0OCIsICJwb3J0IjogIjgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAzIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODExNTM2MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xODYiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTY1OTgwMTM4NTEiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA3IiwgImFkZCI6ICI0NS4xOTkuMTM4LjIyMiIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjRlYzBhZTYyLWRlMDktNDAyOS05MDRhLTAzMTNkNDYyOGVjZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2MjUxNjkzMDQ4IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDkiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY5NDQ4MDY5NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTEiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy40MjA3NzIzMC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTYyNTE1MjI0MzgiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDExIiwgImFkZCI6ICIxNDYuMTkwLjExMC45MiIsICJwb3J0IjogMjIxMTgsICJpZCI6ICJiODAwZmJhNi0yODM1LTRiNDQtODNjMi01Mjc1ZmRiYjI0YmEiLCAiYWlkIjogMCwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJtZWRpYS1leHAxLmxpY2RuLmNvbSIsICJwYXRoIjogIi8iLCAidGxzIjogIm5vbmUifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAiYWRkIjogInd3dy43NTQwOTg1NC54eXoiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpoZzloNUtwTW1KTGxpNlc2UWpkMnlp@us02.shawbrothersstudio.com:43642#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E6%96%B0%E5%9B%BD%E4%BF%A1%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2016
```

