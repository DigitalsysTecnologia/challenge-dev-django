FROM node

WORKDIR /app

COPY package.json .
RUN npm i

COPY . .

EXPOSE 5173

COPY ./entrypoint.sh /
