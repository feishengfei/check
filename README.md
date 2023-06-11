
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr               | cn          | cc   | isp                                           | ip             | chatgpt          |
|---:|:---------------------|:-------------------|:------------|:-----|:----------------------------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 192.74.243.57      | China       | CN   | PEGTECHINC                                    | 137.175.8.81   | Yes (Region: US) |
|  1 | [3](config/3.json)   | 156.225.67.111     | Netherlands | NL   | YISP B.V.                                     | 154.84.1.140   | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.245.8.141      | Netherlands | NL   | YISP B.V.                                     | 154.84.1.139   | Yes (Region: NL) |
|  3 | [6](config/6.json)   | turkey.abraak.site | Turkey      | TR   | Teknosos Bilisim Hizmetleri Ve Tic. Ltd. Sti. | 212.64.214.179 | Yes (Region: TR) |
|  4 | [8](config/8.json)   | www.noice.id       | Germany     | DE   | AS-GLOBALTELEHOST                             | 193.108.118.34 | Yes (Region: DE) |
|  5 | [12](config/12.json) | 8.v2-ray.cyou      | Japan       | JP   | AMAZON-02                                     | 18.179.36.139  | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgImFkZCI6ICIxOTIuNzQuMjQzLjU3IiwgInBvcnQiOiAiNDMyNDYiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTExIiwgInBvcnQiOiAiMzI5MzMiLCAiaWQiOiAiYjhkZjNlZjEtODg3Zi00ZWU0LTg1NWYtNGY4MDQxNmMyNDY0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0MSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYxOTMxMTZkLTk2ZjktNGQ3YS05YmU1LTViYjA2YTY5YWYwYiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTgyMywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAidHVya2V5LmFicmFhay5zaXRlIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NGYwYVx1NjcxNyAgNiIsICJwb3J0IjogMjA4NywgImlkIjogIjIxMDI1ODM5LWMxNDAtNGM2Ny04ZjRjLTlhNDEzY2E4ZGUzZiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInd3dy5ub2ljZS5pZCIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICIzNzc3NjAxOS0wN2VhLTRhMWQtOTRlNy04OGU1ZTEzM2FkNWEiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInYycmF5MS51ZHBndy5jb20iLCAicGF0aCI6ICIvd29ycnlmcmVlIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

