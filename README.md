
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                               | ip                    | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:----------------------------------|:----------------------|:-----------------|
|  0 | [1](config/1.json)   | hinet1261.gfwisbest.xyz  | Taiwan        | TW   | Data Communication Business Group | 1.171.219.239         | Yes (Region: TW) |
|  1 | [3](config/3.json)   | 156.225.67.250           | Netherlands   | NL   | YISP B.V.                         | 154.84.1.36           | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.225.67.85            | Netherlands   | NL   | YISP B.V.                         | 154.84.1.232          | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 156.245.8.105            | Netherlands   | NL   | YISP B.V.                         | 154.84.1.128          | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 156.225.67.125           | Netherlands   | NL   | YISP B.V.                         | 154.84.1.158          | Yes (Region: NL) |
|  5 | [8](config/8.json)   | rnrn3g.555456.xyz        | Germany       | DE   | Hetzner Online GmbH               | 116.202.230.160       | Yes (Region: DE) |
|  6 | [13](config/13.json) | 4.mamadcucu.com          | Finland       | FI   | Hetzner Online GmbH               | 2a01:4f9:c011:605c::1 | Yes (Region: FI) |
|  7 | [15](config/15.json) | new3.hucloud-dns.xyz     | United States | US   | PONYNET                           | 209.141.33.7          | Yes (Region: US) |
|  8 | [16](config/16.json) | 3.mamadcucu.com          | Finland       | FI   | Hetzner Online GmbH               | 2a01:4f9:c011:752c::1 | Yes (Region: FI) |
|  9 | [19](config/19.json) | germany1.unlimiteddev.co | Germany       | DE   | Hetzner Online GmbH               | 116.202.230.160       | Yes (Region: DE) |

## Valid
```
vmess://eyJhZGQiOiAiaGluZXQxMjYxLmdmd2lzYmVzdC54eXoiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU2NWIwXHU1MzE3XHU1ZTAyXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxIDEiLCAicG9ydCI6IDIyNCwgImlkIjogIjIyODUxMzNlLWI5YmEtM2ZiNS1hMjQ2LTljN2RkY2MyY2Q3YSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4yNTAiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIzZmQ2MzdhZC00NmZlLTRmODUtYTZlOC04NmIwMGJjYTExMjIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk5MjAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny44NSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjEzMGM5ZjJlLTQyYjEtNGViZi1iMzQ1LWUyNjQ1NmEwNjFmOSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTkyMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjEwNSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImZlNWY2OWU3LWUxODMtNDM5Yi05NTBiLTk2NjFlZjA2NTFmMiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzMDc3OSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xMjUiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIzYTNjOGE5Yy0zMzRlLTQzNjAtYWRiOC1hODBhNTdkZGNiYmYiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDM5MjIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAicm5ybjNnLjU1NTQ1Ni54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjE3YzZjNjRlLWViM2MtNDRhZS05OGY4LWQ0Njk3MTNmOTFmMSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvbHBrdXZ3cyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNC5tYW1hZGN1Y3UuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIjQubWFtYWRjdWN1LmNvbSIsICJpZCI6ICI1MWJhNWE5YS00YjdjLTRjNjItYjRhZS0wZTUzZWM4ZDMwMjQiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0Fyc2FsYW5UYXVCb3QiLCAicG9ydCI6ICI4ODgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAibmV3My5odWNsb3VkLWRucy54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjFjOGFkM2YyLTgzNWMtNGZkYS1iOWI2LTg4MWQzY2FkZmQ4ZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTUiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMy5tYW1hZGN1Y3UuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIjMubWFtYWRjdWN1LmNvbSIsICJpZCI6ICI5MjkzNDRlMS00NzNjLTRmZWItYjg2Yi1mZGUzZWUxY2NkMTYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0Fyc2FsYW5UYXVCb3QiLCAicG9ydCI6ICIyMDg2IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxNiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE5IiwgImFkZCI6ICJnZXJtYW55MS51bmxpbWl0ZWRkZXYuY28iLCAicG9ydCI6ICI4MCIsICJpZCI6ICI5N2VhNzlhNi02MTVjLTRhZDctODA4My00ZjNiNDljYmU4YTIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImdlcm1hbnkxLnVubGltaXRlZGRldi5jbyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

