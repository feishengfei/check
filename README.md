
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn   | cc   | isp   | ip            | chatgpt          |
|---:|:---------------------|:--------------------|:-----|:-----|:------|:--------------|:-----------------|
|  0 | [2](config/2.json)   | 137.175.9.205       |      |      |       | 142.4.118.225 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 51.195.125.16       |      |      |       | 51.89.42.212  | Yes (Region: GB) |
|  2 | [4](config/4.json)   | 156.225.67.73       |      |      |       | 154.84.1.19   | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 156.249.18.158      |      |      |       | 154.84.1.134  | Yes (Region: NL) |
|  4 | [8](config/8.json)   | cfcdn.sanfencdn.net |      |      |       | 23.225.9.234  | Yes (Region: US) |
|  5 | [9](config/9.json)   | 107.167.7.12        |      |      |       | 107.167.18.50 | Yes (Region: US) |
|  6 | [11](config/11.json) | 154.85.1.245        |      |      |       | 154.84.1.206  | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDIiLCAiYWRkIjogIjEzNy4xNzUuOS4yMDUiLCAicG9ydCI6ICI1NzkwMiIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNTEuMTk1LjEyNS4xNiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1NDkwMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4MmYxXHU1NmZkXHU3OTNlXHU0ZjFhXHU0ZmRkXHU5NjY5XHU1Yjg5XHU1MTY4XHU5MGU4IDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICI1MzEyMyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMjExNTVlZmQtOGUyOS00M2QyLTk1YmMtZmUzMTkwZWNiMWM2IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4xNTgiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDgxMjMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZVx1OGM2YVx1NzY3Ylx1NzcwMVx1N2VhNlx1N2ZmMFx1NTE4NVx1NjVhZlx1NTgyMUNsb3VkaW5ub3ZhdGlvblx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmY2RuLnNhbmZlbmNkbi5uZXQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiZjExNGU2ZDktMGNkYS00ZmU4LWI3NjktM2JjZWIzYmNhNDUzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1czQuc2FuZmVuY2RuMS5jb20iLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyIsICJzbmkiOiAidXMxLnNhbmZlbmNkbjEuY29tIn0=
vmess://eyJhZGQiOiAiMTA3LjE2Ny43LjEyIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJiZGVlMjAyYy04ZmFlLTQ0MWYtYTU4OC03YmM0ZDM4ODcwMTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0MTY1NCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlx1NWUwMlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA5IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTEiLCAiYWRkIjogIjE1NC44NS4xLjI0NSIsICJwb3J0IjogIjQ3NzMxIiwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZmFcdWQ4M2NcdWRkZjhVU1x1N2Y4ZVx1NTZmZCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
```

