
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn            | cc   | isp                             | ip             | chatgpt          |
|---:|:---------------------|:----------------------|:--------------|:-----|:--------------------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 67.21.64.84           | United States | US   | SHARKTECH                       | 67.21.72.34    | Yes (Region: US) |
|  1 | [5](config/5.json)   | 45.199.138.176        | United States | US   | NovoServe B.V.                  | 45.199.138.43  | Yes (Region: US) |
|  2 | [6](config/6.json)   | 986.outline-vpn.cloud | Netherlands   | NL   | YISP B.V.                       | 154.84.1.194   | Yes (Region: NL) |
|  3 | [8](config/8.json)   | 156.225.67.243        | Poland        | PL   | OVH SAS                         | 54.36.174.181  | Yes (Region: FR) |
|  4 | [22](config/22.json) | 172.64.130.176        | Spain         | ES   | NIXVAL                          | 213.162.210.46 | Yes (Region: ES) |
|  5 | [27](config/27.json) | vfly3.win             | Japan         | JP   | Alibaba US Technology Co., Ltd. | 47.245.30.19   | Yes (Region: JP) |
|  6 | [30](config/30.json) | 17.wyhkaa0.gq         | United States | US   | SPRINTLINK                      | 45.146.82.67   | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiNjcuMjEuNjQuODQiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQzMTIzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE3NiIsICJwb3J0IjogIjQ5ODUyIiwgImlkIjogIjZmYTU2MGQ0LTM1YzUtNDk2OC1hZGZjLTgxMmM1Mjg3OGI4NCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiOTg2Lm91dGxpbmUtdnBuLmNsb3VkIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiYTdmYThmMTQtNGZiNi00MjgwLTkwMDUtZDZiYmU5OWM1ZGE5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6ICI0NjQxMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDgiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjQzIiwgInBvcnQiOiAiNDM1ODIiLCAiaWQiOiAiOTkwMDA2YmQtY2IyMC00ODJmLTljOTctZjVmYzY1MzU5NjA1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTcyLjY0LjEzMC4xNzYiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAieGJ5LmRhb3poYW5nLmxpbmsiLCAiaWQiOiAiZjI5ODJkYjItMjNlMy00MzBiLWFmNTQtZTgzYmE4NDIwNWZkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIiIsICJwb3J0IjogIjgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAyMiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI3IiwgImFkZCI6ICJ2Zmx5My53aW4iLCAicG9ydCI6ICI0NDMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjk2ODFmOTllLWQyNTEtNDc3YS1kNzc3LTFkMDFlZTU1MDQ4MSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvbXlibG9nIiwgImhvc3QiOiAidmZseTMud2luIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDMwIiwgImFkZCI6ICIxNy53eWhrYWEwLmdxIiwgInBvcnQiOiAyMDk1LCAiaWQiOiAiMWUzNjY1NWItN2QyOC00NTEzLWQ3ZjgtNWYxYTBjMDBhMDdkIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICIxNy53eWhrYWEwLmdxIiwgInBhdGgiOiAiL1RHOkBoa2FhMCIsICJ0bHMiOiAiIn0=
```

