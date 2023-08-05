
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp           | ip                                  | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:--------------|:------------------------------------|:-----------------|
|  0 | [8](config/8.json)   | dongtaiwang2.com | Netherlands   | NL   | CLOUDFLARENET | 2a09:bac1:5560::20a:2a              | Yes (Region: NL) |
|  1 | [11](config/11.json) | a13.2e5bf271.win | Singapore     | SG   | AMAZON-02     | 52.77.221.89                        | Yes (Region: SG) |
|  2 | [13](config/13.json) | 45.92.161.166    | United States | US   | DEDIPATH-LLC  | 45.83.117.170                       | Yes (Region: US) |
|  3 | [20](config/20.json) | 156.249.18.38    | Netherlands   | NL   | YISP B.V.     | 2a02:2a38:1:2796:ec4:7aff:fe81:7d76 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmMgIDYiLCAiYWRkIjogImEwOC4yZTViZjI3MS53aW4iLCAicG9ydCI6ICI4MCIsICJpZCI6ICJiN2ViM2ZmZC02MmZlLTQ5NmQtOWJiMi1lZGQyMWVkODc3ZjIiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDciLCAiYWRkIjogImRvbmd0YWl3YW5nMi5jb20iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiMjVhOWYzYjktMWU2ZC00MGJkLTk2OGItZTA4MThjMWIxOTZmIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIyLmZyZWVrMS54eXoiLCAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1YjBcdTUyYTBcdTU3NjFBbWF6b25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogImExMy4yZTViZjI3MS53aW4iLCAicG9ydCI6ICI4MCIsICJpZCI6ICJiN2ViM2ZmZC02MmZlLTQ5NmQtOWJiMi1lZGQyMWVkODc3ZjIiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZiMjdcdTc2ZGYgIDEyIiwgImFkZCI6ICI0NS45Mi4xNjEuMTY2IiwgInBvcnQiOiAiNDc5MjkiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTkiLCAiYWRkIjogIjE1Ni4yNDkuMTguMzgiLCAicG9ydCI6ICI0ODIyMiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXMuY2FzaGRhd2lvZHhrYXdqYWlvY2pkYXdkYXdkYWR3cmF3Z2ZzZWdzZWRlZHdhZGF3ZmdyZHJjdnNzc2wudG9wIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
```

