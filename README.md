
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn             | cc   | isp                 | ip                                 | chatgpt          |
|---:|:---------------------|:---------------------|:---------------|:-----|:--------------------|:-----------------------------------|:-----------------|
|  0 | [6](config/6.json)   | 156.225.67.138       | Netherlands    | NL   | YISP B.V.           | 154.84.1.137                       | Yes (Region: NL) |
|  1 | [8](config/8.json)   | 13.224.250.76        | United States  | US   | AS-GLOBALTELEHOST   | 169.197.141.187                    | Yes (Region: US) |
|  2 | [14](config/14.json) | 156.225.67.19        | Netherlands    | NL   | YISP B.V.           | 154.84.1.194                       | Yes (Region: NL) |
|  3 | [15](config/15.json) | 172.99.190.149       | United Kingdom | GB   | AS-GLOBALTELEHOST   | 172.99.190.149                     | Yes (Region: GB) |
|  4 | [29](config/29.json) | 38.64.138.145        | United States  | US   | AS-GLOBALTELEHOST   | 38.64.138.145                      | Yes (Region: US) |
|  5 | [31](config/31.json) | 172.99.190.149       | United Kingdom | GB   | AS-GLOBALTELEHOST   | 172.99.190.149                     | Yes (Region: GB) |
|  6 | [34](config/34.json) | hax1.freeair.eu.org  | Germany        | DE   | Hetzner Online GmbH | 2a01:4f8:140:229c:107c:6491:7de9:1 | Yes (Region: DE) |
|  7 | [35](config/35.json) | 104.17.3.81          | Singapore      | SG   | DIGITALOCEAN-ASN    | 104.248.146.201                    | Yes (Region: SG) |
|  8 | [36](config/36.json) | new3.hucloud-dns.xyz | United States  | US   | PONYNET             | 209.141.33.7                       | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xMzgiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5NjRiZjQ5OS05ZWMwLTQzNzgtOTJiNi04N2Q4ZDg2MWIyZDAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk5MjAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTMuMjI0LjI1MC43NiIsICJhaWQiOiAwLCAiaG9zdCI6ICJkcHk3ZnUxMXJ4bjV4LmNsb3VkZnJvbnQubmV0IiwgImlkIjogIjYwMWJiNzcxLWQzNWMtNDdjZS1mNDQwLTI5NWRhZWJlN2QzZiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvYWxpc3QiLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRYZXJveCA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE0IiwgImFkZCI6ICIxNTYuMjI1LjY3LjE5IiwgInBvcnQiOiAiMzczODEiLCAiaWQiOiAiYTdmYThmMTQtNGZiNi00MjgwLTkwMDUtZDZiYmU5OWM1ZGE5IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@172.99.190.149:8090#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2015
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@38.64.138.145:2376#github.com/freefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2029
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@172.99.190.149:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2031
vmess://eyJhZGQiOiAiaGF4MS5mcmVlYWlyLmV1Lm9yZyIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMmNhMTUzMTgtMTAxNS00ODZkLWVmM2UtNDY1MjEwMmEyMzVhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9oYXgxIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAzNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTA0LjE3LjMuODEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAzNSIsICJwb3J0IjogODAsICJpZCI6ICJlNDBiMmRlMy1iODI5LTQ1OTEtYTdiNi05OWQxOTEzZjMyNDYiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAidy5ldm91Y2g3Ny5saXZlIiwgInBhdGgiOiAiL3dvcnJ5ZnJlZSIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAibmV3My5odWNsb3VkLWRucy54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAibmV3My5odWNsb3VkLWRucy54eXoiLCAiaWQiOiAiMWM4YWQzZjItODM1Yy00ZmRhLWI5YjYtODgxZDNjYWRmZDhlIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAzNiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

