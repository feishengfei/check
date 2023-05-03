
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn            | cc   | isp                    | ip                   | chatgpt          |
|---:|:---------------------|:-----------------------|:--------------|:-----|:-----------------------|:---------------------|:-----------------|
|  0 | [2](config/2.json)   | 172.245.206.3          | United States | US   | SERVER-MANIA           | 172.245.206.3        | Yes (Region: US) |
|  1 | [5](config/5.json)   | join-bede.vmessorg.fun | Germany       | DE   | Hetzner Online GmbH    | 2a01:4f8:192:348a::2 | Yes (Region: DE) |
|  2 | [8](config/8.json)   | hd.mamadcucu.com       | United States | US   | AS-GLOBALTELEHOST      | 169.197.141.187      | Yes (Region: US) |
|  3 | [9](config/9.json)   | new6.huvicloud.com     | United States | US   | PONYNET                | 199.195.251.9        | Yes (Region: US) |
|  4 | [19](config/19.json) | vus3.0bad.com          | United States | US   | Akamai Connected Cloud | 66.175.222.252       | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTcyLjI0NS4yMDYuMyIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiM2Q4N2YwZGItYzlmZC00NWY1LTg4YjEtNDY5OTc4YTQxZDNlIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI4ODkzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU3ZWJkXHU3ZWE2XHU1ZGRlXHU0ZjBhXHU1MjI5XHU1M2JmXHU1YTAxXHU1ZWM5XHU2NWFmXHU3ZWY0XHU1YzE0XHU2NzUxQ29sb0Nyb3NzaW5nXHU2NzA5XHU5NjUwXHU1MTZjXHU1M2Y4IDIiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiam9pbi1iZWRlLnZtZXNzb3JnLmZ1biIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiYjkxMTA1YzktMjA2MS00MGU2LTkyMTktZDA0ZDViNDg2OWQzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI4MCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OWE2Y1x1Njc2NVx1ODk3Zlx1NGU5YVRtbmV0XHU1OTI3XHU5YTZjXHU3NTM1XHU4YmFmIDUiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiaGQubWFtYWRjdWN1LmNvbSIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICJoNC5tYW1hZGN1Y3UuY29tIiwgImlkIjogIjhlZDlhZWMyLWUwMmUtNGEyNy1mZTAyLWMzZTIwNDUyZTRjNyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiMjA1MiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgOCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAibmV3Ni5odXZpY2xvdWQuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJhMTFjYTc2MC05ZWY5LTRhNjMtOTVjOS00YzVjMzJkNTYyNTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2h1dmkiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA5IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAidnVzMy4wYmFkLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9jaGF0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1OGQzOVx1NTIyOVx1ODQ5OUxpbm9kZVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxOSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

