
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn        | cc   | isp                             | ip                                     | chatgpt          |
|---:|:---------------------|:----------------------------|:----------|:-----|:--------------------------------|:---------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 120.233.43.37               | Hong Kong | HK   | CNSERVERS                       | 172.247.18.66                          | Yes (Region: US) |
|  1 | [3](config/3.json)   | cctv.iepl01.yuntiair365.top | Singapore | SG   | ORACLE-BMC-31898                | 129.150.61.168                         | Yes (Region: SG) |
|  2 | [16](config/16.json) | 47.236.123.100              | Singapore | SG   | Alibaba US Technology Co., Ltd. | 47.236.123.100                         | Yes (Region: SG) |
|  3 | [19](config/19.json) | 45.121.48.196               | Taiwan    | TW   | EMGINECONCEPT-01                | 45.121.48.196                          | Yes (Region: TW) |
|  4 | [21](config/21.json) | 64.176.47.200               | Japan     | JP   | AS-CHOOPA                       | 2401:c080:3800:3ba0:5400:4ff:feaa:a942 | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMiIsICJhZGQiOiAiMTIwLjIzMy40My4zNyIsICJwb3J0IjogIjUyNjI5IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiY2N0di5pZXBsMDEueXVudGlhaXIzNjUudG9wIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICI0MGRiODVmMS0yMjNmLTM3NGYtYTQ5YS1kYmM5NzM2YzQzMGYiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTMwMDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWU3Zlx1NGUxY1x1NzcwMVx1NzlmYlx1NTJhOCAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgMTYiLCAiYWRkIjogIjQ3LjIzNi4xMjMuMTAwIiwgInBvcnQiOiAiMzM2ODEiLCAiaWQiOiAiNzIwMmQxMWYtMjc1OS00ZDhjLWUxZDEtMTRjYjEzOGU0MjA1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDE5IiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiMGVkMzU2MjktOTE5YS00ODkxLWJhMGYtMTNjZDE5OGY4NjNiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWEgMjEiLCAiYWRkIjogIjY0LjE3Ni40Ny4yMDAiLCAicG9ydCI6ICIyOTQxNCIsICJpZCI6ICI0ZDVlOGFhMi0wNjQxLTQzMjMtZTkyYy0yYzA2MWNkYzhlMzQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

