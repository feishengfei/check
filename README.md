
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp              | ip              | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:-----------------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | 141.147.153.244  | Japan         | JP   | ORACLE-BMC-31898 | 141.147.153.244 | Yes (Region: JP) |
|  1 | [4](config/4.json)   | 37.120.193.102   | Serbia        | RS   | M247 Europe SRL  | 146.70.111.194  | Yes (Region: RS) |
|  2 | [5](config/5.json)   | 51vfly1.win      | Germany       | DE   | Contabo GmbH     | 5.189.166.24    | Yes (Region: DE) |
|  3 | [8](config/8.json)   | dongtaiwang3.com | Poland        | PL   | OVH SAS          | 54.36.174.181   | Yes (Region: FR) |
|  4 | [10](config/10.json) | 64.32.21.246     | United States | US   | SHARKTECH        | 107.167.24.162  | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTQxLjE0Ny4xNTMuMjQ0IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJkNDdkNzEzNS0wOTU0LTQ2YWItYTE5MC0xN2I2Yzg2MzBhODUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDE1NDUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NzQ1ZVx1NTE3OE9yYWNsZSBDb3Jwb3JhdGlvbiAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMzcuMTIwLjE5My4xMDIiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI1NzE3MGZmMC03MTgwLTQ2NjQtOGY2MS04ZGViZGRhMzQ1ZjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjUyOTIwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjU3XHU5YTZjXHU1YzNjXHU0ZTlhICA0IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiNTF2Zmx5MS53aW4iLCAiYWlkIjogMCwgImhvc3QiOiAiNTF2Zmx5MS53aW4iLCAiaWQiOiAiOTY4MWY5OWUtZDI1MS00NzdhLWQ3NzctMWQwMWVlNTUwNDgxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9teWJsb2ciLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA1IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDgiLCAiYWRkIjogImRvbmd0YWl3YW5nMy5jb20iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNmRlZGRiN2YtZTU1Ny00MmRiLWJmYTAtY2Y0MGIzNmIyN2UyIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJkLmZyZWVoMS54eXoiLCAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwgInRscyI6ICJ0bHMiLCAic25pIjogImQuZnJlZWgxLnh5eiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjY0LjMyLjIxLjI0NiIsICJwb3J0IjogIjQ0MzEzIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI1N2Y5M2U5Mi1lYmI5LTRmMTYtOWJkYy04MjI1ZDIwMTA5OTUiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
```

