
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr                        | cn            | cc   | isp              | ip                                  | chatgpt          |
|---:|:-------------------|:----------------------------|:--------------|:-----|:-----------------|:------------------------------------|:-----------------|
|  0 | [1](config/1.json) | 159.203.40.212              | Canada        | CA   | DIGITALOCEAN-ASN | 159.203.40.212                      | Yes (Region: CA) |
|  1 | [3](config/3.json) | 146.190.99.55               | Singapore     | SG   | DIGITALOCEAN-ASN | 146.190.99.55                       | Yes (Region: SG) |
|  2 | [4](config/4.json) | 154.85.1.244                | Netherlands   | NL   | YISP B.V.        | 154.84.1.216                        | Yes (Region: NL) |
|  3 | [5](config/5.json) | 45.199.138.191              | Netherlands   | NL   | YISP B.V.        | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba | Yes (Region: NL) |
|  4 | [6](config/6.json) | 156.225.67.104              | Netherlands   | NL   | YISP B.V.        | 154.84.1.44                         | Yes (Region: NL) |
|  5 | [7](config/7.json) | www.75409854.xyz            | United States | US   | SHARKTECH        | 107.167.22.10                       | Yes (Region: US) |
|  6 | [9](config/9.json) | us02.shawbrothersstudio.com | United States | US   | NETLAB-SDN       | 154.40.56.206                       | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU5LjIwMy40MC4yMTIiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjEzYTQxZjQ3LTViZTItNDYyYi1kODZhLTI3Zjc0ZGVkNmUyYyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNTM3ODciLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUyYTBcdTYyZmZcdTU5MjdcdTViODlcdTU5MjdcdTc1NjVcdTc3MDFcdTU5MWFcdTRmMjZcdTU5MWFEaWdpdGFsT2NlYW5cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiMTQ2LjE5MC45OS41NSIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICJtZWRpYS1leHAxLmxpY2RuLmNvbSIsICJpZCI6ICIwODEzODYyZS1lZmY5LTQ2NjYtY2Y3MC0wMGJlODFkNWNjN2YiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL1NIQUxBTkEiLCAicG9ydCI6ICIyMTcyNSIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODExNTM2MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTEiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy40MjA3NzIzMC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTYyNTE1MjI0MzgiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY5NDQ4MDY5NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICIyOGRkNmMyNi0wNWE1LTRiYmEtOGE1ZC0wNTJiNzBhYzEzYjIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNzU0MDk4NTQueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDQyOTkwODc0OCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpoZzloNUtwTW1KTGxpNlc2UWpkMnlp@us02.shawbrothersstudio.com:43642#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E6%96%B0%E5%9B%BD%E4%BF%A1%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%209
```

