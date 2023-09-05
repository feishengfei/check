
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn          | cc   | isp                            | ip             | chatgpt          |
|---:|:---------------------|:-----------------|:------------|:-----|:-------------------------------|:---------------|:-----------------|
|  0 | [8](config/8.json)   | cfyd.starsea.vip | Poland      | PL   | OVH SAS                        | 54.36.174.181  | Yes (Region: FR) |
|  1 | [13](config/13.json) | 156.225.67.38    | Netherlands | NL   | YISP B.V.                      | 154.84.1.16    | Yes (Region: NL) |
|  2 | [15](config/15.json) | 172.64.153.211   | Sweden      | SE   | Stark Industries Solutions Ltd | 94.131.115.68  | Yes (Region: SE) |
|  3 | [18](config/18.json) | cloudqwq.cf      | France      | FR   | SYNLINQ                        | 103.252.90.249 | Yes (Region: FR) |
|  4 | [20](config/20.json) | 23.158.56.89     | Germany     | DE   | AS-GLOBALTELEHOST              | 23.158.56.89   | Yes (Region: DE) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmeWQuc3RhcnNlYS52aXAiLCAicG9ydCI6ICI4MCIsICJpZCI6ICJjNjc0N2RhNC1mYjJlLTRhMmEtYmRiNy04NjE0YmRkNmIwYjMiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInNnMS12MnJheS5zc2hraXQub3JnIiwgInBhdGgiOiAiL3NzaGtpdC8xNzM2OTYwMTExLzY0ZWUyNjA0MWVmY2MvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4zOCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDEzIiwgInBvcnQiOiA0NDMsICJpZCI6ICJkZTQ5MTgwMi0yMzNlLTQ3ZjItOGM2Yy1kMTliY2Y1YmQ1NmIiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogInd3dy44NjEzOTMxNy54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjkyMjU2OTAyNDMwIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE1IiwgImFkZCI6ICIxNzIuNjQuMTUzLjIxMSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI2ZTc1MTcxMi05NTY5LTUxODctODZlYS04ZjU4NWFkOTkxMDUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInBhdGgiOiAiL2FwaTAxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiY2xvdWRxd3EuY2YiLCAiYWlkIjogMCwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAiaWQiOiAiY2QwYzU3MGYtNzU3Yy00OGQyLWExYjYtYzA5NDA0MzFjYzQ3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTdmOGVcdTU3MzBcdTUzM2EgIDIwIiwgImFkZCI6ICIyMy4xNTguNTYuODkiLCAicG9ydCI6ICIyMjMyNCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMDQ2MjFiYWUtYWIzNi0xMWVjLWI5MDktMDI0MmFjMTIwMDAyIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
```

