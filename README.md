
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp                              | ip                    | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:---------------------------------|:----------------------|:-----------------|
|  0 | [2](config/2.json)   | 156.225.67.223      | Netherlands   | NL   | YISP B.V.                        | 154.84.1.136          | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 156.225.67.136      | Netherlands   | NL   | YISP B.V.                        | 154.84.1.137          | Yes (Region: NL) |
|  2 | [6](config/6.json)   | cfcdn.sanfencdn.net | United States | US   | Eons Data Communications Limited | 65.75.220.16          | Yes (Region: US) |
|  3 | [7](config/7.json)   | dl6.v001sssv.pw     | Germany       | DE   | Hetzner Online GmbH              | 2a01:4f8:1c17:4d19::1 | Yes (Region: DE) |
|  4 | [15](config/15.json) | dl.v001sssv.pw      | France        | FR   | OVH SAS                          | 51.77.213.73          | Yes (Region: FR) |
|  5 | [19](config/19.json) | 104.31.16.58        | Germany       | DE   | Hetzner Online GmbH              | 2a01:4f8:1c17:c667::1 | Yes (Region: DE) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4yMjMiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJlYmVjMmFkZi1lOTQwLTQ0NmYtYmVkNC1kOGM5MTE0M2I1NGEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk4MjMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTM2IiwgInBvcnQiOiAiNDkxMjMiLCAiaWQiOiAiOTY0YmY0OTktOWVjMC00Mzc4LTkyYjYtODdkOGQ4NjFiMmQwIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmM1x1ZDgzY1x1ZGRmMU5MXHU4Mzc3XHU1MTcwKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDYiLCAiYWRkIjogImNmY2RuLnNhbmZlbmNkbi5uZXQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiMTVjZWRiMWUtYjZlNy00ZGQ4LWFjNjUtNDIyZTFhMzIyOTcyIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1czEuc2FuZmVuY2RuLm5ldCIsICJwYXRoIjogIi96aC1jbiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICJ1czEuc2FuZmVuY2RuLm5ldCIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDciLCAiYWRkIjogImRsNi52MDAxc3Nzdi5wdyIsICJwb3J0IjogIjgwIiwgImlkIjogIjhlZWNlMmUxLWNmYzEtNGY4NC04MDNlLTFhNjY2NTA5ODJlYSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE1IiwgImFkZCI6ICJkbC52MDAxc3Nzdi5wdyIsICJwb3J0IjogIjgwIiwgImlkIjogImE0YmI3ZjkzLWNlZTYtNDNkNy1iMmRkLWZhOWM3MGI4ODIzMyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZGwudjAwMXNzc3YucHciLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTA0LjMxLjE2LjU4IiwgImFpZCI6ICIwIiwgImFscG4iOiAiaDIsaHR0cC8xLjEiLCAiZnAiOiAicmFuZG9tIiwgImhvc3QiOiAiTWNpLVJpZ2h0ZWwtdGFsaWEtbW9raGFiZXJhdC5pcmFuY2VsbC1pcmFuY2VsbC53ZWJzaXRlIiwgImlkIjogImExMGY5ZDI0LWJiNWQtNDYyMi1lNzViLWYwMmMzNDg1MDZhOSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvQFNleXllZE1UIEBTZXl5ZWRNVCIsICJwb3J0IjogIjQ0MyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTkiLCAic2N5IjogImF1dG8iLCAic25pIjogIk1jaTItUmlnaHRlbC10YWxpYS1tb2toYWJlcmF0LmlyYW5jZWxsLWlyYW5jZWxsLndlYnNpdGUiLCAidGxzIjogInRscyIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
```

