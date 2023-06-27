
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                    | cn            | cc   | isp                        | ip             | chatgpt          |
|---:|:---------------------|:------------------------|:--------------|:-----|:---------------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 67.21.84.214            | United States | US   | SHARKTECH                  | 67.21.85.2     | Yes (Region: US) |
|  1 | [4](config/4.json)   | 172.247.67.46           | United States | US   | CNSERVERS                  | 23.225.9.234   | Yes (Region: US) |
|  2 | [5](config/5.json)   | 156.225.67.136          | Netherlands   | NL   | YISP B.V.                  | 154.84.1.137   | Yes (Region: NL) |
|  3 | [6](config/6.json)   | 156.225.67.52           | Netherlands   | NL   | YISP B.V.                  | 154.84.1.37    | Yes (Region: NL) |
|  4 | [8](config/8.json)   | zfc.windowsupdate1.com  | Germany       | DE   | AS-GLOBALTELEHOST          | 193.108.118.34 | Yes (Region: DE) |
|  5 | [12](config/12.json) | akrab2.v-pn.my.id       | Taiwan        | TW   | PT Cloud Hosting Indonesia | 103.52.115.229 | Yes (Region: TW) |
|  6 | [19](config/19.json) | cn-to-hk-443.db-link.in | Singapore     | SG   | Datacamp Limited           | 5.180.78.163   | Yes (Region: SG) |

## Valid
```
vmess://eyJhZGQiOiAiNjcuMjEuODQuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYjlhMzA1YTktMWZmMi00ZWMxLWIzMzgtOTMzNTU1ODMzYmFhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ3MDg4LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDb3BlcmF0aW9uIENvbG9jdGlvblx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgImFkZCI6ICIxNzIuMjQ3LjY3LjQ2IiwgInBvcnQiOiAiNTAwMzUiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjIyNzhlZmU0LWFkMGMtNDdjZS05NDgwLTA2ODYwODM2OGQ3NiIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTM2IiwgInBvcnQiOiAiNDc4NTIiLCAiaWQiOiAiOTY0YmY0OTktOWVjMC00Mzc4LTkyYjYtODdkOGQ4NjFiMmQwIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNTIiLCAicG9ydCI6ICI1MjQ0OSIsICJpZCI6ICI5OTAwMDZiZC1jYjIwLTQ4MmYtOWM5Ny1mNWZjNjUzNTk2MDUiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInpmYy53aW5kb3dzdXBkYXRlMS5jb20iLCAicG9ydCI6IDgwLCAiaWQiOiAiMDE5MjUxNjktZTJmZi00ODNjLTg5ZjItNmU3NzhkY2RkNDUwIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ1cy0xLmFjeXVuLmNmIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiYWtyYWIyLnYtcG4ubXkuaWQiLCAiYWlkIjogMCwgImhvc3QiOiAiaWRjOC52cG4tYWtjZWxsdWxlci5teS5pZCIsICJpZCI6ICJiMDdhMzQ5Yi01ZTNjLTRiMTctYWFiZS1kMWRjNjMzNzZlY2YiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3YycmF5IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTIiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZjYjNcdTUzMTdcdTc3MDFcdTc1MzVcdTRmZTEgMTkiLCAiYWRkIjogImNuLXRvLWhrLTQ0My5kYi1saW5rLmluIiwgInBvcnQiOiA0NDMsICJpZCI6ICI0MGNiYzc1MC1hMTgyLTNmZTItODgzMi05ZmE2MDA2MzU0Y2YiLCAiYWlkIjogMSwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImZyZWUtdG8tdXMtMDEuZGItbGluay5pbiIsICJwYXRoIjogIi9kYiIsICJ0bHMiOiAidGxzIn0=
```

