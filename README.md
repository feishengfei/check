
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn             | cc   | isp       | ip            | chatgpt          |
|---:|:---------------------|:---------------------|:---------------|:-----|:----------|:--------------|:-----------------|
|  0 | [3](config/3.json)   | 156.245.8.241        | Netherlands    | NL   | YISP B.V. | 154.84.1.44   | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 156.225.67.169       | Netherlands    | NL   | YISP B.V. | 154.84.1.121  | Yes (Region: NL) |
|  2 | [8](config/8.json)   | 154.85.1.244         | Poland         | PL   | OVH SAS   | 54.36.174.181 | Yes (Region: FR) |
|  3 | [15](config/15.json) | ci.outline-vpn.cloud | United States  | US   | SHARKTECH | 67.21.72.34   | Yes (Region: US) |
|  4 | [16](config/16.json) | 120.226.50.91        | United Kingdom | GB   | OVH SAS   | 51.89.40.141  | Yes (Region: GB) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjI0MSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1MTI0NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNjkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJiZDI0OWUzNy03MzU5LTQxZWUtODRhNy0wOWU0OWUwZWM1YzQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzU5NzcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQxNDUzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTUiLCAiYWRkIjogImNpLm91dGxpbmUtdnBuLmNsb3VkIiwgInBvcnQiOiAiNDMxMjMiLCAiaWQiOiAiMjU2NmQwMGYtMjE4Yy00OGY3LTlhMzYtMTNkM2Q2ZjFhNzI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZlNTZcdTUzNTdcdTc3MDFcdTc5ZmJcdTUyYTggMTYiLCAiYWRkIjogIjEyMC4yMjYuNTAuOTEiLCAicG9ydCI6ICI0NzAwOSIsICJpZCI6ICI4M2E0MjRkOC00YmNiLTRjZWUtYjAxNi0yYzhmMWRiNGE5MjEiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

