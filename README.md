
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp           | ip                                 | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:--------------|:-----------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 107.167.29.93            | United States | US   | SHARKTECH     | 107.167.9.234                      | Yes (Region: US) |
|  1 | [3](config/3.json)   | 64.32.21.246             | United States | US   | SHARKTECH     | 107.167.24.162                     | Yes (Region: US) |
|  2 | [7](config/7.json)   | 67.21.84.216             | United States | US   | SHARKTECH     | 67.21.85.2                         | Yes (Region: US) |
|  3 | [8](config/8.json)   | cf-lt.sharecentre.online | United States | US   | MULTA-ASN1    | 2607:f130:109:0:225:90ff:fe79:7d34 | Yes (Region: US) |
|  4 | [31](config/31.json) | Shopify.com              | France        | FR   | CLOUDFLARENET | 2a09:bac5:3264:be::13:298          | Yes (Region: FR) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTA3LjE2Ny4yOS45MyIsICJwb3J0IjogIjQ1NTg1IiwgImlkIjogIjQ2NWRlYzFhLWUwOWItNGJiNi05OTA1LTcwZjc1ZDYwMzVjOCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiNjQuMzIuMjEuMjQ2IiwgInBvcnQiOiAiNDQzMTMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjU3ZjkzZTkyLWViYjktNGYxNi05YmRjLTgyMjVkMjAxMDk5NSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9wYXRoLzE2ODk1ODg0OTc3NjUiLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNjcuMjEuODQuMjE2IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA3IiwgInBvcnQiOiA0NzA4OCwgImlkIjogImI5YTMwNWE5LTFmZjItNGVjMS1iMzM4LTkzMzU1NTgzM2JhYSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjVmNzUxYzZlLTUwYjEtNDc5Ny1iYThlLTZmZmUzMjRhMGJjZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZHAzLnNjcHJveHkudG9wIiwgInBhdGgiOiAiL3NoaXJrZXIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDMxIiwgImFkZCI6ICJTaG9waWZ5LmNvbSIsICJwb3J0IjogIjIwODYiLCAiaWQiOiAiMjUwZjQzMzEtOGMzZS00Yjg3LWE4NmItNWM1ZmJmOWRkYmE4IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJGci5jbG91ZGZsYXJlLnF1ZXN0IiwgInBhdGgiOiAiL2FyaWVzIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

