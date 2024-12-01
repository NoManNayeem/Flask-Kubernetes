FROM node:20-alpine

WORKDIR /app

# Copy the package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the source code and the .env file explicitly
COPY . .
COPY .env .env

# Build the React app
RUN npm run build

# Serve the app
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
