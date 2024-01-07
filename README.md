
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn   | cc   | isp   | ip             | chatgpt          |
|---:|:---------------------|:---------------|:-----|:-----|:------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 51.145.68.57   |      |      |       | 51.145.68.57   | Yes (Region: GB) |
|  1 | [3](config/3.json)   | 51.142.75.225  |      |      |       | 51.142.75.225  | Yes (Region: GB) |
|  2 | [5](config/5.json)   | 51.158.150.168 |      |      |       | 51.158.150.168 | Yes (Region: FR) |
|  3 | [6](config/6.json)   | 142.4.96.211   |      |      |       | 142.0.131.49   | Yes (Region: US) |
|  4 | [15](config/15.json) | 51.142.73.20   |      |      |       | 51.142.73.20   | Yes (Region: GB) |
|  5 | [18](config/18.json) | 45.87.153.246  |      |      |       | 45.87.153.246  | Yes (Region: NL) |
|  6 | [25](config/25.json) | 38.54.108.222  |      |      |       | 38.54.108.222  | Yes (Region: US) |
|  7 | [26](config/26.json) | 38.68.134.202  |      |      |       | 38.68.134.202  | Yes (Region: US) |
|  8 | [27](config/27.json) | 38.68.134.202  |      |      |       | 38.68.134.202  | Yes (Region: US) |
|  9 | [41](config/41.json) | 38.54.185.112  |      |      |       | 192.74.239.146 | Yes (Region: US) |
| 10 | [42](config/42.json) | 38.54.185.111  |      |      |       | 192.74.239.146 | Yes (Region: US) |
| 11 | [44](config/44.json) | 217.160.45.31  |      |      |       | 217.160.45.31  | Yes (Region: DE) |
| 12 | [49](config/49.json) | 156.249.18.66  |      |      |       | 154.84.1.122   | Yes (Region: NL) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpLbEpsWFhlOUtqUVg0bWg0eEMwNWM5@51.145.68.57:13751#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%202
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpPRVlobFZRbVAxbmVkSUlJbE1nTm01@51.142.75.225:47430#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%203
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@51.158.150.168:4444#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E5%B7%B4%E9%BB%8EOnline%20S.A.S%205
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA2IiwgImFkZCI6ICIxNDIuNC45Ni4yMTEiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICIyYTIzZGJkNS0wOWNmLTRhYTgtYTgzNS0zMjMwNzI4YzQ5NzMiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuOTIzMDg5MDcueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwNDA5NTEyMjc3OCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp0QW9XenVLdk5PUHJzTGM0ZkFFT25v@51.142.73.20:6961#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Microsoft%E5%85%AC%E5%8F%B8%2015
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%2018
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@38.54.108.222:8119#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2025
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.68.134.202:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2026
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@38.68.134.202:8091#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2027
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggNDEiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzM2NjQ5OTkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMTA5MTEzMzQwOSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggNDIiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzM2NjQ5OTkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMDY1NzYyNTE4MSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMjE3LjE2MC40NS4zMSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNGUxODY2NzgtZmNjYS00MzI1LWU0YmMtYjI5MTZiZGY2NzA4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDg4ODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NWZiN1x1NTZmZE9uZUFuZE9uZVx1NTE2Y1x1NTNmOCA0NCIsICJzY3kiOiAiYWVzLTEyOC1nY20iLCAidGxzIjogIm5vbmUiLCAidHlwZSI6ICJub25lIiwgInYiOiAyfQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNDkiLCAiYWRkIjogIjE1Ni4yNDkuMTguNjYiLCAicG9ydCI6ICIzMTAwMCIsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNzIyODExNDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwNDI3NjQ2Njc2MCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

