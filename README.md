
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp                    | ip              | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:-----------------------|:----------------|:-----------------|
|  0 | [4](config/4.json)   | 156.245.8.240        | Netherlands   | NL   | YISP B.V.              | 154.84.1.44     | Yes (Region: NL) |
|  1 | [10](config/10.json) | 198.2.202.215        | United States | US   | PEGTECHINC             | 107.148.194.225 | Yes (Region: US) |
|  2 | [16](config/16.json) | 156.245.8.151        | Netherlands   | NL   | YISP B.V.              | 154.84.1.148    | Yes (Region: NL) |
|  3 | [19](config/19.json) | cfcdn3.sanfencdn.net | Singapore     | SG   | Akamai Connected Cloud | 172.104.161.252 | Yes (Region: US) |
|  4 | [29](config/29.json) | 198.211.9.182        | United States | US   | MULTA-ASN1             | 198.211.9.182   | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQiLCAiYWRkIjogIjE1Ni4yNDUuOC4yNDAiLCAicG9ydCI6ICI0NTMyNiIsICJpZCI6ICIyOWE1ZDQ4ZS0yNGYxLTQ4ZmQtYTVlMS05YTQ2Y2IzMTAzMmYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiXHVkODNjXHVkZGYzXHVkODNjXHVkZGYxTkxcdTgzNzdcdTUxNzAoeW91dHViZVx1OTYzZlx1NGYxZlx1NzlkMVx1NjI4MCkiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDgiLCAiYWRkIjogIjEwMy4xODQuNDUuMTc1IiwgInBvcnQiOiAiMjA4MiIsICJpZCI6ICIwYWZiOGIyYy0xNDlhLTQ5YTgtZTkwZi1kNzc4ODRhYzkyMmYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImVjYy52dGNzcy50b3AiLCAicGF0aCI6ICIvYmx1ZTA5IiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyAxMCIsICJhZGQiOiAiMTk4LjIuMjAyLjIxNSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuMTMzNjQ4OTYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5MTQwMzU0MDU3NyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICJ3d3cuMTMzNjQ4OTYueHl6In0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDE2IiwgImFkZCI6ICIxNTYuMjQ1LjguMTUxIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjg0ZDFkZTExLWNlMTItNGExNS04MzEyLTEzMzgzNTZkNGFjNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy41NzQyNDM0OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjkxNTc1OTE5NzIyIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiY2ZjZG4zLnNhbmZlbmNkbi5uZXQiLCAiYWlkIjogMCwgImhvc3QiOiAic2czLnNhbmZlbmNkbjIuY29tIiwgImlkIjogIjE2NTgyNzU5LTNkMjAtNDgwNC05YzljLWE1OGFkN2IyNjBhOCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvemgtY24iLCAicG9ydCI6IDIwNTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTkiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTk4LjIxMS45LjE4MiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGM5MGQxNjctZTY1Yi00NDE5LWQ0NTUtZWI2MzU3MjRkMmVkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDM3ODY5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyOSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

