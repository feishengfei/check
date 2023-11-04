
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn             | cc   | isp                    | ip             | chatgpt          |
|---:|:---------------------|:----------------------|:---------------|:-----|:-----------------------|:---------------|:-----------------|
|  0 | [4](config/4.json)   | cfcdn2.sanfencdn9.com | Singapore      | SG   | Akamai Connected Cloud | 139.144.117.95 | Yes (Region: US) |
|  1 | [5](config/5.json)   | 156.225.67.106        | Netherlands    | NL   | YISP B.V.              | 154.84.1.44    | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 45.199.138.146        | Netherlands    | NL   | YISP B.V.              | 154.84.1.122   | Yes (Region: NL) |
|  3 | [10](config/10.json) | 104.16.67.38          | United Kingdom | GB   | AS-GLOBALTELEHOST      | 172.99.190.86  | Yes (Region: GB) |
|  4 | [11](config/11.json) | 146.190.94.141        | Singapore      | SG   | DIGITALOCEAN-ASN       | 146.190.94.141 | Yes (Region: SG) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDQiLCAiYWRkIjogImNmY2RuMi5zYW5mZW5jZG45LmNvbSIsICJwb3J0IjogIjIwNTIiLCAiaWQiOiAiNTA2ZDkzZWMtZmZkYi00MWNkLWJiYzMtMzY3MDM5YzRiMThmIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzZzM2Yzk5NzRlNC5xY3J5ZWNodnF3Lnh5eiIsICJwYXRoIjogIi92aWRlby9iRlZEbkF5biIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xMDYiLCAidiI6IDIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNSIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJ0bHMiOiAidGxzIiwgInBhdGgiOiAiL3BhdGgvMTY5ODY3MTYwMDk4NiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0NiIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjRlYzBhZTYyLWRlMDktNDAyOS05MDRhLTAzMTNkNDYyOGVjZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4OTMyNDAxNTc3IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTA0LjE2LjY3LjM4IiwgImFpZCI6IDAsICJob3N0IjogImFsdnZpbi5jbGljayIsICJpZCI6ICIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCAibmV0IjogIndzIiwgInBhdGgiOiAibGlua3Z3cyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEwIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTQ2LjE5MC45NC4xNDEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICAxMSIsICJwb3J0IjogNDIzNTgsICJpZCI6ICI2ZTRlZGJkOC03ODU0LTRlZjUtYzljNi00OWU5NTgyMmU0ZmMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAibWVkaWEtZXhwMS5saWNkbi5jb20iLCAicGF0aCI6ICIvQE9OSElUX0VISSIsICJ0bHMiOiAiIn0=
```

