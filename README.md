
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn            | cc   | isp                              | ip                                  | chatgpt          |
|---:|:---------------------|:----------------------------|:--------------|:-----|:---------------------------------|:------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 154.85.1.244                | Netherlands   | NL   | YISP B.V.                        | 154.84.1.216                        | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 146.190.99.55               | Singapore     | SG   | DIGITALOCEAN-ASN                 | 146.190.99.55                       | Yes (Region: SG) |
|  2 | [5](config/5.json)   | 156.225.67.104              | Netherlands   | NL   | YISP B.V.                        | 154.84.1.44                         | Yes (Region: NL) |
|  3 | [13](config/13.json) | cfcdn3.sanfencdn9.com       | Japan         | JP   | Eons Data Communications Limited | 38.207.152.110                      | Yes (Region: US) |
|  4 | [17](config/17.json) | www.75409854.xyz            | United States | US   | SHARKTECH                        | 107.167.22.10                       | Yes (Region: US) |
|  5 | [18](config/18.json) | us02.shawbrothersstudio.com | United States | US   | NETLAB-SDN                       | 154.40.56.206                       | Yes (Region: US) |
|  6 | [19](config/19.json) | 146.190.110.92              | Singapore     | SG   | DIGITALOCEAN-ASN                 | 146.190.110.92                      | Yes (Region: SG) |
|  7 | [22](config/22.json) | 45.199.138.191              | Netherlands   | NL   | YISP B.V.                        | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODExNTM2MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiMTQ2LjE5MC45OS41NSIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICJtZWRpYS1leHAxLmxpY2RuLmNvbSIsICJpZCI6ICIwODEzODYyZS1lZmY5LTQ2NjYtY2Y3MC0wMGJlODFkNWNjN2YiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL1NIQUxBTkEiLCAicG9ydCI6ICIyMTcyNSIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgNCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY5NDQ4MDY5NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiY2ZjZG4zLnNhbmZlbmNkbjkuY29tIiwgImFpZCI6IDAsICJob3N0IjogImpwMTdhYWI3MmE3LmNodnNpZmV0cmoueHl6IiwgImlkIjogIjJjZjQ3MmQ0LTcxYWEtNDYzOS05OGM5LWJkMTNlMTY0OWUxMyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvdmlkZW8vdXViQ2RKdEsiLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTciLCAiYWRkIjogInd3dy43NTQwOTg1NC54eXoiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpoZzloNUtwTW1KTGxpNlc2UWpkMnlp@us02.shawbrothersstudio.com:43642#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E6%96%B0%E5%9B%BD%E4%BF%A1%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2018
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDE5IiwgImFkZCI6ICIxNDYuMTkwLjExMC45MiIsICJwb3J0IjogMjIxMTgsICJpZCI6ICJiODAwZmJhNi0yODM1LTRiNDQtODNjMi01Mjc1ZmRiYjI0YmEiLCAiYWlkIjogMCwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJtZWRpYS1leHAxLmxpY2RuLmNvbSIsICJwYXRoIjogIi8iLCAidGxzIjogIm5vbmUifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTEiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy40MjA3NzIzMC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTYyNTE1MjI0MzgiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAyMiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

