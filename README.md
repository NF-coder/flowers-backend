# TODO List:
- [ ] DOCUMENTATION!
- [ ] Replace some @dataclass constants to env variables in .env files
- [ ] SessionId + JWT
- [ ] GRPC encryption
- [ ] New grpc exceptions handling (bypassing them in json)

# Structure
```
├── .backend/               # Директория с предыдущей версией приложения
├── v2/                     # Директория с микросервисами
    ├── db_services/        # Сервисы, взаимодействующие с СУЬД. В перспективе заменяем их на go
    ├── buisness_logic/     # Слой бизнес-логики. Полумонолит
    ├── rest_gateway/       # Шлюз для http-траффика
    ├── images_uploader/    # Микросервис + http-шлюз для загрузки медиа. Отделён для упрощения вынесения на отдельный сервер
    └── rest_gateway_nginx/ # Nginx в качестве reverse-proxy для http-шлюзов
└── docs/                   # Документация (пишется)
```

# Docs overview
## Databse
Main atabase schema
![schema](https://github.com/NF-coder/flowers-backend/blob/master/docs/db/diagram.png?raw=true)
You also can edit this schema and see it's deatails by loading .dbml file from [/docs/db/](https://github.com/NF-coder/flowers-backend/tree/master/docs/db) to [drawdb](https://www.drawdb.app/editor)
