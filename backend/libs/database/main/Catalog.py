import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from .Basic import Basic
from .ProductAdditionalImages import ProductAdditionalImages
from .Users import Users

from ..backend.api.CatalogAPI import CatalogAPI
from ..backend.fields.CatalogDB import CatalogDB

class Catalog(Basic):
    @classmethod
    async def start(self) -> Self:
        '''
            Method that starts connection to database
            Returns:
                `Catalog` object
        '''
        return await self.start_(CatalogAPI, CatalogDB, SecurityConfig.DATABASE_URL)
    
    
    async def add_product(self,
        title: str,
        titleImageUrl: str,
        costNum: int,
        description: str,
        authorId: int
    ) -> int:
        '''
            Method that creates product
        '''
        '''
            За отсутствием резиновой уточки проблемы архитектуры решалиь так. 
            В тексте нет никакой важности для стороннего разработчика, можно смело пропускать    
        
            И тут я понял, что при проектировании допустил огромную ошибку...

            В чём заключается ошибка?
                А как мне вытянуть ключ продукта при его создании для передачи его в другие сущности (additionalImages)? А никак)
                Нужно пользоваться возможностями ORM для создания дополнительных сущностей сразу вместе с основным объектом.
                
                Нужно как-то реализовать передачу данных между различными модулями ORM.
            Возможные решения:
                1) Перепроектирование с 0. Явно видно, что данный уровень абстракции выполняет непонятно какие ф-ии
                    Текущая архитектура:
                        1) Low-level api
                            1 функция - 1 запрос. Здесь ТОЛЬКО создаются и отправляются запросы
                        2) Middleware
                            Это абстракция над запросами. Тут производятся различные операции по подготовке данных.
                        3) RESTful api
                    P.S. Чёт я всё это написал, и тепер этот уровень абстракции не кажется лишним.
            
            Так, стоп. По сути я только что выяснил, что ничего менять (по крайней мере сильно) не надо.
                Есть 2 пути:
                    1) инициализируем по несколько low-level api в одном middleware классе
                    2) передаём один middleware класс в другой
                Пока выбираю вариант #2, затем можно будет переписать, благо апи небольшое

            К сожалению такой вариант оказался плохим из-за крайне непонятных плавающих багов.
            Временно рализую без relations и foreignKey 
        '''

        return await self.api.create_product(
            title=title,
            titleImageUrl=titleImageUrl,
            costNum=costNum,
            description=description,
            authorId=authorId
        )
    
    async def get_my_products(
            self,
            userId: int,
            start: int,
            count: int,
            sort: str
        ) -> list:
        if sort == "time_descending":
            return await self.api.get_my_products_time_desc(
                userId = userId,
                start = start,
                count = count
            )
        elif sort == "time_upscending":
            return await self.api.get_my_products_time_upsc(
                    userId = userId,
                    start = start,
                    count = count
                )
        else:
            raise Developing("Sorry, this sort type is unimplemeted. We're already working on it...")
        
    async def get_product_by_id(
            self,
            id: int
        ) -> dict:
        return (await self.api.get_product_by_id(
            productId=id
        ))[0]
    
    async def get_products(
            self,
            start: int,
            count: int,
            sort: str
        ) -> list:
        if sort == "time_descending":
            return await self.api.get_all_products_time_desc(
                start = start,
                count = count
            )
        elif sort == "time_upscending":
            return await self.api.get_all_products_time_upsc(
                    start = start,
                    count = count
                )
        else:
            raise Developing("Sorry, this sort type is unimplemeted. We're already working on it...")
    
    # BAD SEARCH FUNCTION! REWRITE IT!
    async def search_in_title(
            self,
            phrase: str,
            start: int,
            count: int,
            sort: str
        ) -> list:
        '''
        out = []
        for word in phrase.split():
            out.extend(
                await self.api.search_title_contains(phrase)
            )
        return list(set(sorted(out, key=lambda x: out.count(x), reverse=True)))
        '''
        if sort == "time_descending":
            return await self.api.search_title_contains_time_desc(
                phrase,
                start,
                count
            )
        elif sort == "time_upscending":
            return await self.api.search_title_contains_time_upsc(
                phrase,
                start,
                count
            )
        else:
            raise Developing("Sorry, this sort type is unimplemeted. We're already working on it...")
        
