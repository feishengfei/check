
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn             | cc   | isp                 | ip              | chatgpt          |
|---:|:---------------------|:-------------------------|:---------------|:-----|:--------------------|:----------------|:-----------------|
|  0 | [4](config/4.json)   | 194.146.49.64            | United Kingdom | GB   | QuickHostUK Limited | 194.146.49.64   | Yes (Region: GB) |
|  1 | [5](config/5.json)   | new3.hucloud-dns.xyz     | United States  | US   | PONYNET             | 209.141.33.7    | Yes (Region: US) |
|  2 | [6](config/6.json)   | germany1.unlimiteddev.co | Germany        | DE   | Hetzner Online GmbH | 116.202.230.160 | Yes (Region: DE) |
|  3 | [7](config/7.json)   | cf.noaries.de            | Luxembourg     | LU   | PONYNET             | 107.189.28.253  | Yes (Region: LU) |
|  4 | [8](config/8.json)   | 162.159.255.205          | Germany        | DE   | Hetzner Online GmbH | 116.202.230.160 | Yes (Region: DE) |
|  5 | [12](config/12.json) | 85.208.108.21            | Japan          | JP   | ENZUINC             | 85.208.108.18   | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZjZDVcdTU2ZmQgIDQiLCAiYWRkIjogIjE5NC4xNDYuNDkuNjQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiOWM5MTE0M2MtN2NlYS00MTM1LTg5ZDgtZGE4NTE1MTVkZTU1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAibmV3My5odWNsb3VkLWRucy54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAibmV3My5odWNsb3VkLWRucy54eXoiLCAiaWQiOiAiMWM4YWQzZjItODM1Yy00ZmRhLWI5YjYtODgxZDNjYWRmZDhlIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSA1IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDYiLCAiYWRkIjogImdlcm1hbnkxLnVubGltaXRlZGRldi5jbyIsICJwb3J0IjogIjgwIiwgImlkIjogIjk3ZWE3OWE2LTYxNWMtNGFkNy04MDgzLTRmM2I0OWNiZThhMiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZ2VybWFueTEudW5saW1pdGVkZGV2LmNvIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDciLCAiYWRkIjogImNmLm5vYXJpZXMuZGUiLCAicG9ydCI6ICI4MDgwIiwgImlkIjogImEwZjE1M2Q4LWUzMmYtNDFmMy05YmNkLTA3M2Y1NzllMjI2NCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiYnV5dm0uY2xvdWRmbGFyZS5xdWVzdCIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTYyLjE1OS4yNTUuMjA1IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiNTI0NjZkYzItMzU1MC00MzEwLTkxMGMtNzRiN2JmOGEwMjBlIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiaG9zdCI6ICJ1cy0xLmFjeXVuLmV1Lm9yZyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgInR5cGUiOiAibm9uZSIsICJzZXJ2ZXJQb3J0IjogMCwgIm5hdGlvbiI6ICIifQ==
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@85.208.108.21:8118#github.com/freefq%20-%20%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AFArabic%20Computer%20System%20Co.%2012
```

