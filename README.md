
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp                              | ip                        | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:---------------------------------|:--------------------------|:-----------------|
|  0 | [2](config/2.json)   | 192.74.228.172      | China         | CN   | PEGTECHINC                       | 142.0.129.201             | Yes (Region: US) |
|  1 | [12](config/12.json) | 156.225.67.138      | Netherlands   | NL   | YISP B.V.                        | 154.84.1.137              | Yes (Region: NL) |
|  2 | [13](config/13.json) | cf.noaries.de       | Italy         | IT   | CLOUDFLARENET                    | 2a09:bac5:422a:187::27:84 | Yes (Region: IT) |
|  3 | [16](config/16.json) | cfcdn.sanfencdn.net | United States | US   | Eons Data Communications Limited | 65.75.221.195             | Yes (Region: US) |
|  4 | [17](config/17.json) | 104.18.1.74         | Finland       | FI   | Hetzner Online GmbH              | 2a01:4f9:c010:baec::1     | Yes (Region: DE) |

## Valid
```
vmess://eyJhZGQiOiAiMTkyLjc0LjIyOC4xNzIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDI4NTcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDEyIiwgImFkZCI6ICIxNTYuMjI1LjY3LjEzOCIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI5NjRiZjQ5OS05ZWMwLTQzNzgtOTJiNi04N2Q4ZDg2MWIyZDAiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuODE2NzgwMzQueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4NDQ5MjUzNjIzNiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEzIiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAiMjA1MiIsICJpZCI6ICI2N2M1Y2U0NS03YjQ4LTQ3M2UtYmYyNS1lNGM4MzBiMGVkMjQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImF6c3R1LWl0LmlpaW8ud2lraSIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICJjZmNkbi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImRkODMxNGNjLTM3NTQtNDE2ZC05NDU2LTA5OTFmMmU3NDc1MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXMyLnNhbmZlbmNkbi5uZXQiLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTA0LjE4LjEuNzQiLCAiYWlkIjogIjAiLCAiaG9zdCI6ICJoLmgzaW8uY28iLCAiaWQiOiAiNDA4ZTI2ODYtOWUwZC00MDE0LTg0MWUtN2NhNWRhNTVhMjE1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogImhvM2lubyIsICJwb3J0IjogIjIwOTYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE3IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICJoLmgzaW8uY28iLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAidiI6ICIyIn0=
```

