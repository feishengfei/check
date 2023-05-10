
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr                     | cn            | cc   | isp                    | ip              | chatgpt          |
|---:|:-------------------|:-------------------------|:--------------|:-----|:-----------------------|:----------------|:-----------------|
|  0 | [2](config/2.json) | 156.225.67.125           | Netherlands   | NL   | YISP B.V.              | 154.84.1.158    | Yes (Region: NL) |
|  1 | [3](config/3.json) | 156.245.8.93             | Netherlands   | NL   | YISP B.V.              | 154.84.1.178    | Yes (Region: NL) |
|  2 | [4](config/4.json) | 156.245.8.188            | Netherlands   | NL   | YISP B.V.              | 154.84.1.40     | Yes (Region: NL) |
|  3 | [5](config/5.json) | vus2.0bad.com            | United States | US   | Akamai Connected Cloud | 45.79.114.248   | Yes (Region: US) |
|  4 | [6](config/6.json) | 156.225.67.231           | Netherlands   | NL   | YISP B.V.              | 154.84.1.219    | Yes (Region: NL) |
|  5 | [8](config/8.json) | cf-lt.sharecentre.online | United States | US   | AS-GLOBALTELEHOST      | 169.197.141.187 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDIiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTI1IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjNhM2M4YTljLTMzNGUtNDM2MC1hZGI4LWE4MGE1N2RkY2JiZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4xNjA0NjYyNi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjgzNjI5MzE0OTE1IiwgInRscyI6ICJ0bHMiLCAic25pIjogInd3dy4xNjA0NjYyNi54eXoifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDMiLCAiYWRkIjogIjE1Ni4yNDUuOC45MyIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI5MzUwM2RkNS0yNDVhLTRlYjEtYWUyYS01N2FiOWYyYjNjMjkiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNDc3MzQ2NDcueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4MzYyOTMxNDkxNSIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQiLCAiYWRkIjogIjE1Ni4yNDUuOC4xODgiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNWE0ZDY5YWQtMjBhOS00OTQxLWIyMjMtODdiYmQwOWY1ZjUyIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQ4NjQzNzAwLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2ODM2MjkzMTQ5MTUiLCAidGxzIjogInRscyIsICJzbmkiOiAid3d3LjQ4NjQzNzAwLnh5eiJ9
vmess://eyJhZGQiOiAidnVzMi4wYmFkLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9jaGF0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1OGQzOVx1NTIyOVx1ODQ5OUxpbm9kZVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA1IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjMxIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjUxNWJjYjRkLTBiYTEtNGNhZS04N2NmLWEwNDcwMDdlZWM1NCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy43MzkzODAyMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjgzNjI5MzE0OTE1IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjJkNWQ4YjljLThlYzQtNGEzNy1iNjEwLTc4ZTcxZTEzZWFlZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAibHYxLnNoYXJlY2VudHJlcHJvLm9yZyIsICJwYXRoIjogIi9zaGlya2VyIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

