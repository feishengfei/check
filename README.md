
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                 | ip              | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:--------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 156.225.67.61            | Netherlands   | NL   | YISP B.V.           | 154.84.1.139    | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 154.85.0.3               | Netherlands   | NL   | YISP B.V.           | 154.84.1.229    | Yes (Region: NL) |
|  2 | [5](config/5.json)   | 208.76.54.103            | United States | US   | Netrouting          | 208.76.54.103   | Yes (Region: US) |
|  3 | [11](config/11.json) | germany1.unlimiteddev.co | Germany       | DE   | Hetzner Online GmbH | 116.202.230.160 | Yes (Region: DE) |
|  4 | [14](config/14.json) | 156.225.67.106           | Netherlands   | NL   | YISP B.V.           | 154.84.1.44     | Yes (Region: NL) |
|  5 | [15](config/15.json) | 85.208.108.94            | Japan         | JP   | ENZUINC             | 85.208.108.90   | Yes (Region: JP) |
|  6 | [21](config/21.json) | 154.85.0.7               | Netherlands   | NL   | YISP B.V.           | 154.84.1.122    | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDIiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNjEiLCAicG9ydCI6ICI0OTk1NSIsICJpZCI6ICI2MTkzMTE2ZC05NmY5LTRkN2EtOWJlNS01YmIwNmE2OWFmMGIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU0Ljg1LjAuMyIsICJwb3J0IjogIjUzNDQ1IiwgImlkIjogImQzMTMzNDg0LWYyYmYtNGIwYy04ZDM4LWY4ZTY0NWI2NTY4NyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMjA4Ljc2LjU0LjEwMyIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiYmEzN2Y2NTctNDM3YS00ZWY2LWI3ZjMtMTY0MjcyYTEzYmE5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDU3ODUzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTRmNWJcdTdmNTdcdTkxY2NcdThmYmVcdTVkZGVcdThmYzhcdTk2M2ZcdTViYzZOZXRyb3V0aW5nXHU1MTZjXHU1M2Y4IDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDExIiwgImFkZCI6ICJnZXJtYW55MS51bmxpbWl0ZWRkZXYuY28iLCAicG9ydCI6ICI4MCIsICJpZCI6ICI5N2VhNzlhNi02MTVjLTRhZDctODA4My00ZjNiNDljYmU4YTIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImdlcm1hbnkxLnVubGltaXRlZGRldi5jbyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xMDYiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIyOWE1ZDQ4ZS0yNGYxLTQ4ZmQtYTVlMS05YTQ2Y2IzMTAzMmYiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk5MjAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMTQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@85.208.108.94:443#github.com/freefq%20-%20%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AFArabic%20Computer%20System%20Co.%2015
vmess://eyJhZGQiOiAiMTU0Ljg1LjAuNyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjRlYzBhZTYyLWRlMDktNDAyOS05MDRhLTAzMTNkNDYyOGVjZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MjIyMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIxIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

