
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                              | ip                                   | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:---------------------------------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.99.77              | China         | CN   | PEGTECHINC                       | 142.4.99.65                          | Yes (Region: US) |
|  1 | [3](config/3.json)   | 154.85.1.79              | Netherlands   | NL   | YISP B.V.                        | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 104.21.29.207            | Finland       | FI   | Hetzner Online GmbH              | 2a01:4f9:c010:baec::1                | Yes (Region: DE) |
|  3 | [8](config/8.json)   | cf-lt.sharecentre.online | United States | US   | AS-GLOBALTELEHOST                | 169.197.141.187                      | Yes (Region: US) |
|  4 | [10](config/10.json) | 158.69.122.231           | Canada        | CA   | OVH SAS                          | 158.69.122.231                       | Yes (Region: CA) |
|  5 | [12](config/12.json) | cfcdn.sanfencdn.net      | United States | US   | Eons Data Communications Limited | 65.75.221.195                        | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTQyLjQuOTkuNzciLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMzNzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuNzkiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjc0M2JkYzg3LTFkZWEtNDFiZi1hYTBiLTUxZGZiYmZlYzhhYSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNDg4MjkiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiMTA0LjIxLjI5LjIwNyIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICJoLmgzaW8uY28iLCAiaWQiOiAiNDA4ZTI2ODYtOWUwZC00MDE0LTg0MWUtN2NhNWRhNTVhMjE1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogImhvM2lubyIsICJwb3J0IjogIjIwOTYiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDYiLCAic2N5IjogImF1dG8iLCAic25pIjogImguaDNpby5jbyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjJkNWQ4YjljLThlYzQtNGEzNy1iNjEwLTc4ZTcxZTEzZWFlZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidWsxLnNjcHJveHkudG9wIiwgInBhdGgiOiAiL3NoaXJrZXIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp4a3VkNWhu@158.69.122.231:80#github.com/freefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%E9%AD%81%E5%8C%97%E5%85%8B%E7%9C%81%E5%8D%9A%E9%98%BF%E5%8A%AA%E7%93%A6OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2010
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICJjZmNkbi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImRkODMxNGNjLTM3NTQtNDE2ZC05NDU2LTA5OTFmMmU3NDc1MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXMyLnNhbmZlbmNkbi5uZXQiLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

