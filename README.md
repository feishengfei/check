
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn             | cc   | isp             | ip                                     | chatgpt          |
|---:|:---------------------|:----------------------|:---------------|:-----|:----------------|:---------------------------------------|:-----------------|
|  0 | [8](config/8.json)   | 104.27.65.218         | United Kingdom | GB   | OVH SAS         | 2001:41d0:800:29c6:857f:29b2:6359:3c2f | Yes (Region: GB) |
|  1 | [19](config/19.json) | cdn.ikuan.dev         | United Kingdom | GB   | OVH SAS         | 2001:41d0:800:29c6:857f:29b2:6359:3c2f | Yes (Region: GB) |
|  2 | [25](config/25.json) | freenodecdn.ikuan.dev |                |      |                 | 2001:41d0:800:29c6:857f:29b2:6359:3c2f | Yes (Region: GB) |
|  3 | [31](config/31.json) | iepl2.airtcp.vip      |                |      |                 | 91.220.203.204                         | Yes (Region: US) |
|  4 | [35](config/35.json) | 8.v2-ray.cyou         |                |      |                 | 18.179.36.139                          | Yes (Region: JP) |
|  5 | [36](config/36.json) | ieplhk.lanyunshi.top  | United States  | US   | M247 Europe SRL | 91.220.203.204                         | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjEwNC4yNy42NS4yMTgiLCAicG9ydCI6ICI4ODgwIiwgImlkIjogImNiOGNiYmMzLTEzN2EtNDA2NC04ZDAyLWIwZWUzY2EyYzE4YyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidG91LnZ0Y3NzLnRvcCIsICJwYXRoIjogIi9xYXp4Y3YwMCIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiY2RuLmlrdWFuLmRldiIsICJhaWQiOiAwLCAiaG9zdCI6ICJmcmVlZm9yZ2Z3LmlrdWFuLmRldiIsICJpZCI6ICIzMTg1YzJmMy00MjQ2LTQ5YzQtYmE4YS01ZWE4ZmIyZWY2YjgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0ZyZWVGb3JHRlciLCAicG9ydCI6IDIwNTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NGUzYlx1NjgzOVx1NTdkZlx1NTQwZFx1NjcwZFx1NTJhMVx1NTY2OFx1NTE2OFx1NzQwM1x1N2IyYzA2T0YxM1x1NTNmN0YuUk9PVC1TRVJWRVJTXHU4MjgyXHU3MGI5KFdvcmxkQW55Y2FzdFx1NGVmYlx1NjRhZFx1N2Y1MVx1N2VkY1x1NGU5Mlx1ODA1NFx1N2Y1MVx1N2NmYlx1N2VkZlx1NTM0Zlx1NGYxYVx1OGZkMFx1NGY1Y0JJTkQ5XHU4ZjZmXHU0ZWY2KSAxOSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiZnJlZW5vZGVjZG4uaWt1YW4uZGV2IiwgImFpZCI6IDAsICJob3N0IjogImZyZWVmb3JnZncuaWt1YW4uZGV2IiwgImlkIjogIjMxODVjMmYzLTQyNDYtNDljNC1iYThhLTVlYThmYjJlZjZiOCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvRnJlZUZvckdGVyIsICJwb3J0IjogMjA1MiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4OTdmXHU3M2VkXHU3MjU5ICAyNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTZkZjFcdTU3MzNcdTVlMDJcdTc5ZmJcdTUyYTggMzEiLCAiYWRkIjogImllcGwyLmFpcnRjcC52aXAiLCAicG9ydCI6ICI1MTAwMiIsICJpZCI6ICIxYTc2ODBkZi04MWExLTNkODktYTIyMS1kYjgxYWM0YjA0ZGYiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJpZXBsMi5haXJ0Y3AudmlwIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMzUiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTZkZjFcdTU3MzNcdTVlMDJcdTc5ZmJcdTUyYTggMzYiLCAiYWRkIjogImllcGxoay5sYW55dW5zaGkudG9wIiwgInBvcnQiOiAiNTEwMDQiLCAiaWQiOiAiMWE3NjgwZGYtODFhMS0zZDg5LWEyMjEtZGI4MWFjNGIwNGRmIiwgImFpZCI6ICIyIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiaWVwbGhrLmxhbnl1bnNoaS50b3AiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

