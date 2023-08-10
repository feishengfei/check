
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn             | cc   | isp            | ip                                   | chatgpt          |
|---:|:---------------------|:----------------|:---------------|:-----|:---------------|:-------------------------------------|:-----------------|
|  0 | [6](config/6.json)   | 45.199.138.192  | Netherlands    | NL   | YISP B.V.      | 2a02:2a38:1:2796:ae1f:6bff:fe9b:29e6 | Yes (Region: NL) |
|  1 | [8](config/8.json)   | 103.184.45.14   | United States  | US   | AS40676        | 108.181.22.205                       | Yes (Region: US) |
|  2 | [11](config/11.json) | 45.199.138.74   | United States  | US   | NovoServe B.V. | 45.199.138.43                        | Yes (Region: US) |
|  3 | [18](config/18.json) | 135.125.166.199 | United Kingdom | GB   | OVH SAS        | 51.89.7.16                           | Yes (Region: GB) |
|  4 | [19](config/19.json) | 54.38.154.130   | Germany        | DE   | OVH SAS        | 2001:41d0:700:1c5a::                 | Yes (Region: FR) |
|  5 | [22](config/22.json) | 51.89.68.17     | Germany        | DE   | OVH SAS        | 2001:41d0:700:2c84::                 | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTIiLCAiYWlkIjogNjQsICJob3N0IjogInVzMi5teWJlc3Rqai5jb20iLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvMTY1NDQzMSIsICJwb3J0IjogNTUwMTUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDgiLCAiYWRkIjogIjEwMy4xODQuNDUuMTQiLCAicG9ydCI6ICIyMDgyIiwgImlkIjogIjBhZmI4YjJjLTE0OWEtNDlhOC1lOTBmLWQ3Nzg4NGFjOTIyZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZWNjLnZ0Y3NzLnRvcCIsICJwYXRoIjogIi9ibHVlMDkiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC43NCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjZmYTU2MGQ0LTM1YzUtNDk2OC1hZGZjLTgxMmM1Mjg3OGI4NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzMDkxNywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgMTEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTM1LjEyNS4xNjYuMTk5IiwgImFpZCI6IDEsICJob3N0IjogInd3dy42NjcwMDAzOS54eXoiLCAiaWQiOiAiOWJlZGZlOGEtN2Q2ZC00MTZmLTlmYTgtZDliYTNjYTFiNDllIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzA3MDQxMDA3MjcyMCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDE4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNTQuMzguMTU0LjEzMCIsICJhaWQiOiAxLCAiaG9zdCI6ICJ3d3cuMzMyNjgyMDgueHl6IiwgImlkIjogIjdiZWI0MjgxLWU4ZTQtNDE4My1iMTcyLTI5Yjc4MzkxYWJmZCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8yNTI2MTcwODE5MDMiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2Y2Q1XHU1NmZkT1ZIXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDE5IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNTEuODkuNjguMTciLCAiYWlkIjogMSwgImhvc3QiOiAid3d3LjUyODg5MDk5Lnh5eiIsICJpZCI6ICIyMWE5YmZmMi03MmRlLTRlNjItOTNmZi04YjE1OWY2NmQ4NzUiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMjUyNjE3MDgxOTAzIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NmNkNVx1NTZmZCAgMjIiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

