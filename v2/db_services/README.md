# About

All services from this directory has similar structure
```
└── [service_name]/                   # Имя микросервиса
    └── service/                      # Директоия с кодом микросервиса
        ├── [service_name].py         # Основной файл, дающий внешний доступ по gRPC
        ├── exceptions/               # Директория с исключениями
        └── database/                 # Логика взаимодействия с СУБД
            ├── [service_name]DB.py   # Класс, описывающий таблицу
            ├── BasicAPI.py           # Класс, инициализирующий ORM и соединение с ней
            └── [service_name]API.py  # Класс, предоставляющий методы для работы с ORM. По сути здесь инициализируются и исполняются запросы
        ├── schemas/                  # Pydantic-модели входящих и исходящих данных
        └── simplerpc_tmp/            # Директория с автоматически генерируемыми protobuf-файлами
```
