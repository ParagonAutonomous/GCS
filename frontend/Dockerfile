FROM node:20-slim

WORKDIR /app

# install dependencies
COPY package.json package-lock.json ./
RUN npm install

COPY . .

EXPOSE 3030

CMD ["sh", "-c", "npm install && npm run dev -- --host"]