FROM node:20

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

RUN cp .env.example .env

EXPOSE 3030

CMD ["npm", "run", "dev", "--", "--host"]