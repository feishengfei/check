
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp                              | ip                          | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:---------------------------------|:----------------------------|:-----------------|
|  0 | [2](config/2.json)   | 107.167.29.93       | United States | US   | SHARKTECH                        | 107.167.9.234               | Yes (Region: US) |
|  1 | [8](config/8.json)   | cdn.twitter.now.cc  | United States | US   | Eons Data Communications Limited | 65.75.221.195               | Yes (Region: US) |
|  2 | [11](config/11.json) | cfcdn.sanfencdn.net | United States | US   | Eons Data Communications Limited | 65.75.221.195               | Yes (Region: US) |
|  3 | [12](config/12.json) | scaleway.696960.xyz |               |      |                                  | 2a09:bac5:4e26:1478::20a:28 | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTA3LjE2Ny4yOS45MyIsICJwb3J0IjogIjQ1NTg1IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0NjVkZWMxYS1lMDliLTRiYjYtOTkwNS03MGY3NWQ2MDM1YzgiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNcdTk2M2ZcdTkxY2NcdTRlOTEgOCIsICJhZGQiOiAiY2RuLnR3aXR0ZXIubm93LmNjIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjg3MjgzZmU3LTA4ZTUtNDAzYi1hMGFhLWFkZDdjZDY4YTIzZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAibG8udHdpdHRlaS5tZSIsICJwYXRoIjogIi9pa3VuIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAidnVzMi4wYmFkLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9jaGF0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1OGQzOVx1NTIyOVx1ODQ5OUxpbm9kZVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA5IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDExIiwgImFkZCI6ICJjZmNkbi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImRkODMxNGNjLTM3NTQtNDE2ZC05NDU2LTA5OTFmMmU3NDc1MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXMyLnNhbmZlbmNkbi5uZXQiLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAic2NhbGV3YXkuNjk2OTYwLnh5eiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEyIiwgInBvcnQiOiA0NDMsICJpZCI6ICJlMzU3Y2Q2My1mMWE1LTRjOGUtYzQyZS0yNmRhMTEyMDdmZWUiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiL3Jvb3QvIiwgInRscyI6ICJ0bHMifQ==
```

