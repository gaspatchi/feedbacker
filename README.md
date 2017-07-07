**Feedbacker** - сервис для получения заявок и обращений

**Примеры запросов и ответов**

----------
- `POST` /create - Создание обращения

| Параметр  | Тип    | Описание                                             |
| --------- | ------ | ---------------------------------------------------- |
| type      | string | Тип обращения - feedback/driving/hairdresser/florist |
| firstname | string | Имя                                                  |
| lastname  | string | Фамилия                                              |
| number    | string | Номер                                                |
| email     | string | Электронная почта                                    |
| text      | string | Текст обращения                                      |
```
{
  "type": "driving",
  "firstname": "Никита",
  "lastname": "Бережной",
  "number": "89964177136",
  "email": "nikitoshi@gaspatchi.ru",
  "text": "Test, test, test"
}
```
- `Response`
```
{
    "id": 13
}
```

- `GET` /count/{channel} - Получение количества обращений по конкретному каналу 
- `Response`
```
{
    "count": 10
}
```