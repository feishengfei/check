
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp           | ip                                  | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:--------------|:------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 45.199.138.160       |               |      |               | 46.182.107.129                      | Yes (Region: NL) |
|  1 | [8](config/8.json)   | cfcdn3.sanfencdn.net | Netherlands   | NL   | CLOUDFLARENET | 2a09:bac1:5560::20a:2a              | Yes (Region: NL) |
|  2 | [13](config/13.json) | 156.225.67.230       | Netherlands   | NL   | YISP B.V.     | 154.84.1.219                        | Yes (Region: NL) |
|  3 | [14](config/14.json) | 156.249.18.38        | Netherlands   | NL   | YISP B.V.     | 2a02:2a38:1:2796:ec4:7aff:fe81:7d76 | Yes (Region: US) |
|  4 | [17](config/17.json) | 100.42.70.145        | United States | US   | MULTA-ASN1    | 2607:f130:109:0:d6ae:52ff:febc:e193 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE2MCIsICJwb3J0IjogIjUxMjA1IiwgImlkIjogIjk1NDlhMmNmLTEyOWItNDNhMS04OGRiLWVmN2Y2NDhkZTc0YSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiY2ZjZG4zLnNhbmZlbmNkbi5uZXQiLCAiYWlkIjogMCwgImhvc3QiOiAic2cxLnNhbmZlbmNkbjIuY29tIiwgImlkIjogIjUwMmU0ZmYxLTkyZTAtNGEwZS1iZTBlLTNhMGUzNjUzMGUzZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvemgtY24iLCAicG9ydCI6IDIwNTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDEzIiwgImFkZCI6ICIxNTYuMjI1LjY3LjIzMCIsICJwb3J0IjogIjU5ODAxIiwgImlkIjogIjUxNWJjYjRkLTBiYTEtNGNhZS04N2NmLWEwNDcwMDdlZWM1NCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZWRcdWQ4M2NcdWRkZjBIS1x1OTk5OVx1NmUyZih5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTQiLCAiYWRkIjogIjE1Ni4yNDkuMTguMzgiLCAicG9ydCI6ICI0ODIyMiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXMuY2FzaGRhd2lvZHhrYXdqYWlvY2pkYXdkYXdkYWR3cmF3Z2ZzZWdzZWRlZHdhZGF3ZmdyZHJjdnNzc2wudG9wIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTAwLjQyLjcwLjE0NSIsICJhaWQiOiAiNjQiLCAiZW5jcnlwdGlvbiI6ICJhdXRvIiwgImhvc3QiOiAiIiwgImlkIjogIjZhYWEyZjlmLTdjOTEtNGI1MS1hYTc3LTA1YTgzYTVkNmE0ZCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjQxMjQ1IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2TVVMVEFDT01cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTciLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogZmFsc2UsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInVybF9ncm91cCI6ICJ2MnJheSIsICJ2IjogIjIifQ==
```

