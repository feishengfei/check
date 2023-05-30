
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp              | ip                        | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:-----------------|:--------------------------|:-----------------|
|  0 | [8](config/8.json)   | cf-lt.sharecentre.online | Netherlands   | NL   | YISP B.V.        | 154.84.1.145              | Yes (Region: NL) |
|  1 | [11](config/11.json) | cdn.noice.id             | Singapore     | SG   | DIGITALOCEAN-ASN | 143.198.94.243            | Yes (Region: SG) |
|  2 | [12](config/12.json) | 162.159.35.77            | France        | FR   | FEELB SARL       | 45.145.166.232            | Yes (Region: FR) |
|  3 | [14](config/14.json) | 8.v2-ray.cyou            | Japan         | JP   | AMAZON-02        | 18.179.36.139             | Yes (Region: JP) |
|  4 | [15](config/15.json) | cf.noaries.de            | United States | US   | DEDIPATH-LLC     | 2602:fe90:1a:1::81b7:b0dc | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjJkNWQ4YjljLThlYzQtNGEzNy1iNjEwLTc4ZTcxZTEzZWFlZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAibHYyLnNoYXJlY2VudHJlcHJvLm9yZyIsICJwYXRoIjogIi9zaGlya2VyIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICIxNjIuMTU5LjM1Ljc3IiwgInBvcnQiOiA0NDMsICJpZCI6ICJjOTFjN2NiNS02MDljLTRmYWUtODE4ZS05MTk0YzNkNDY5NjkiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImFmcmhtczEyLmJlc3QtdGl6aS50b3AiLCAicGF0aCI6ICIvbGlua3dzIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTQiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE1IiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAyMDgyLCAiaWQiOiAiNjdjNWNlNDUtN2I0OC00NzNlLWJmMjUtZTRjODMwYjBlZDI0IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJkZWRpcGF0aDIuaWlpby53aWtpIiwgInBhdGgiOiAiL2FyaWVzP2VkPTIwNDgiLCAidGxzIjogIiJ9
```

