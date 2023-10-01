FROM node:lts-alpine

# делаем каталог 'app' текущим рабочим каталогом
WORKDIR /frontend

# копируем оба 'package.json' и 'package-lock.json' (если есть)
COPY --chown=node:node ./package*.json ./

# устанавливаем зависимости проекта
RUN npm i


# копируем файлы и каталоги проекта в текущий рабочий каталог (т.е. в каталог 'app')
COPY --chown=node:node  . .

# собираем приложение для production с минификацией
#RUN npm run build

EXPOSE 8000
CMD ["npm", "run", "dev"]