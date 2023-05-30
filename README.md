
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                    | ip                        | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------------|:--------------------------|:-----------------|
|  0 | [3](config/3.json)   | 45.131.248.140  | United States | US   | DEDIPATH-LLC           | 2402:d0c0:1:bce9::1       | Yes (Region: US) |
|  1 | [8](config/8.json)   | 172.67.147.74   | Netherlands   | NL   | YISP B.V.              | 154.84.1.145              | Yes (Region: NL) |
|  2 | [12](config/12.json) | cdn.noice.id    | Singapore     | SG   | DIGITALOCEAN-ASN       | 143.198.94.243            | Yes (Region: SG) |
|  3 | [20](config/20.json) | 139.144.179.178 | Germany       | DE   | Akamai Connected Cloud | 139.144.179.178           | Yes (Region: DE) |
|  4 | [23](config/23.json) | cf.noaries.de   | United States | US   | DEDIPATH-LLC           | 2602:fe90:1a:1::81b7:b0dc | Yes (Region: US) |
|  5 | [24](config/24.json) | 8.v2-ray.cyou   | Japan         | JP   | AMAZON-02              | 18.179.36.139             | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDMiLCAiYWRkIjogIjQ1LjEzMS4yNDguMTQwIiwgInBvcnQiOiAiNTAwNjgiLCAiaWQiOiAiNTU3ZTUzMmUtZGU0YS00YjNlLTlmYjItNWQzNTVjY2I1ZGE5IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI0NS4xMzEuMjQ4LjE0MCIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjE3Mi42Ny4xNDcuNzQiLCAicG9ydCI6ICIyMDUyIiwgImlkIjogIjAyMjdlZGM0LTg3MzUtNDM3MC1hYzQyLTRlODE0NzkyMGYwYiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidG91LnZ0Y3NzLnRvcCIsICJwYXRoIjogIi9xd2VyMTAiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozODUwODI1OTQ0@139.144.179.178:40248#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2020
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIzIiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAyMDgyLCAiaWQiOiAiNjdjNWNlNDUtN2I0OC00NzNlLWJmMjUtZTRjODMwYjBlZDI0IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJkZWRpcGF0aDIuaWlpby53aWtpIiwgInBhdGgiOiAiL2FyaWVzP2VkPTIwNDgiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMjQiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

