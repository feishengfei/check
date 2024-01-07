
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn              | cc   | isp                            | ip             | chatgpt          |
|---:|:---------------------|:---------------|:----------------|:-----|:-------------------------------|:---------------|:-----------------|
|  0 | [4](config/4.json)   | 45.87.153.246  | The Netherlands | NL   | Stark Industries Solutions Ltd | 45.87.153.246  | Yes (Region: NL) |
|  1 | [5](config/5.json)   | 51.158.150.168 | France          | FR   | Scaleway S.a.s.                | 51.158.150.168 | Yes (Region: FR) |
|  2 | [6](config/6.json)   | 142.4.110.10   | China           | CN   | PEG-SV                         | 142.4.110.1    | Yes (Region: US) |
|  3 | [10](config/10.json) | 154.90.39.63   | Malaysia        | MY   | Kaopu Cloud HK Limited         | 154.90.39.63   | Yes (Region: MY) |
|  4 | [13](config/13.json) | 156.249.18.66  | The Netherlands | NL   | YISP B.V.                      | 154.84.1.122   | Yes (Region: NL) |
|  5 | [24](config/24.json) | 38.68.134.202  | United States   | US   | AS-GLOBALTELEHOST              | 38.68.134.202  | Yes (Region: US) |
|  6 | [32](config/32.json) | 38.54.185.111  | China           | CN   | PEG-SV                         | 192.74.239.146 | Yes (Region: US) |
|  7 | [34](config/34.json) | 38.54.185.112  | China           | CN   | PEG-SV                         | 192.74.239.146 | Yes (Region: US) |
|  8 | [36](config/36.json) | 38.68.134.202  | United States   | US   | AS-GLOBALTELEHOST              | 38.68.134.202  | Yes (Region: US) |
|  9 | [38](config/38.json) | 38.68.134.202  | United States   | US   | AS-GLOBALTELEHOST              | 38.68.134.202  | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmN0VJMGRHV1FNNDJUOGd3TjlDWklq@45.87.153.246:6199#github.com/freefq%20-%20%E6%AC%A7%E7%9B%9F%20%204
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@51.158.150.168:4444#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E5%B7%B4%E9%BB%8EOnline%20S.A.S%205
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA2IiwgImFkZCI6ICIxNDIuNC4xMTAuMTAiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICIwOGZjNDk0My00YzdhLTRhNjktOTI2NS1mYjk2MWVhZWE5MTciLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuMjUyMDgwMTAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMzc1NTYyNTU1OCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTU0LjkwLjM5LjYzIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZlx1NzI3OVx1NTIyYlx1ODg0Y1x1NjUzZlx1NTMzYSAxMCIsICJwb3J0IjogNDUzNDMsICJpZCI6ICIwOGFhODQ5OS1kNjE2LTRmZjEtZDZhYi1jZTBjNTIyODI0YWEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAiYWRkIjogIjE1Ni4yNDkuMTguNjYiLCAicG9ydCI6ICIzMTAwMCIsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNzIyODExNDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwNDI3NjQ2Njc2MCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjMiLCAiYWRkIjogIjQ1LjU4LjE1My4yNCIsICJwb3J0IjogIjMwMDAwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MjQyZjllMC02YjdlLTQyNTctOWU5My03YWQzODAxNWM0NmEiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE3MDIzOTIyNTUzNTUiLCAiaG9zdCI6ICJ3d3cuNzc5MzU3MDcueHl6IiwgInRscyI6ICJ0bHMifQ==
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@38.68.134.202:8091#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2024
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMzIiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzM2NjQ5OTkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMDY1NzYyNTE4MSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMzguNTQuMTg1LjExMiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUzNGVcdTc2ZGJcdTk4N2ZDb2dlbnRcdTkwMWFcdTRmZTFcdTUxNmNcdTUzZjggMzQiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJ3d3cuNzM2NjQ5OTkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMTA5MTEzMzQwOSIsICJ0bHMiOiAidGxzIn0=
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@38.68.134.202:5003#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2036
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@38.68.134.202:2375#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BFCogent%E9%80%9A%E4%BF%A1%E5%85%AC%E5%8F%B8%2038
```

