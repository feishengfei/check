
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr              | cn            | cc   | isp       | ip                                  | chatgpt          |
|---:|:---------------------|:------------------|:--------------|:-----|:----------|:------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 156.249.18.24     | Netherlands   | NL   | YISP B.V. | 2a02:2a38:1:2796:ec4:7aff:fe81:7d76 | Yes (Region: NL) |
|  1 | [8](config/8.json)   | private.sky4g.com | Poland        | PL   | OVH SAS   | 54.36.174.181                       | Yes (Region: FR) |
|  2 | [9](config/9.json)   | 64.32.4.53        | United States | US   | SHARKTECH | 107.167.13.162                      | Yes (Region: US) |
|  3 | [14](config/14.json) | 156.225.67.243    | Netherlands   | NL   | YISP B.V. | 154.84.1.37                         | Yes (Region: NL) |
|  4 | [15](config/15.json) | 172.64.130.176    | Spain         | ES   | NIXVAL    | 213.162.210.46                      | Yes (Region: ES) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4yNCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0Nzg2NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlXHU4YzZhXHU3NjdiXHU3NzAxXHU3ZWE2XHU3ZmYwXHU1MTg1XHU2NWFmXHU1ODIxQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdThkOGFcdTUzNTcgIDgiLCAiYWRkIjogInByaXZhdGUuc2t5NGcuY29tIiwgInBvcnQiOiAiODAiLCAidHlwZSI6ICJub25lIiwgImlkIjogImRmYjkzOTVkLWM4NzItNGJmNS05ZjZhLTc1NDJlZWIzYzY0ZSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvc2t5NGcuY29tIiwgImhvc3QiOiAicHJpdmF0ZS5za3k0Zy5jb20iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMzIuNC41MyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJwb3J0IjogNDM1NTYsICJpZCI6ICI4NjUzMDA0Zi1kZTY3LTQ0YzItOWNjZS1lMDgzMDkzM2ZiMDMiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZmFcdWQ4M2NcdWRkZjhVU1x1N2Y4ZVx1NTZmZCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE0IiwgImFkZCI6ICIxNTYuMjI1LjY3LjI0MyIsICJwb3J0IjogIjQzNTgyIiwgImlkIjogIjk5MDAwNmJkLWNiMjAtNDgyZi05Yzk3LWY1ZmM2NTM1OTYwNSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTcyLjY0LjEzMC4xNzYiLCAiYWlkIjogMCwgImhvc3QiOiAieGJ5LmRhb3poYW5nLmxpbmsiLCAiaWQiOiAiZjI5ODJkYjItMjNlMy00MzBiLWFmNTQtZTgzYmE4NDIwNWZkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

