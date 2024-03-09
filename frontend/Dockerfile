# Use a lightweight Node.js image
FROM node:alpine

# Set the working directory
WORKDIR /app

# Copy only package.json and package-lock.json to leverage Docker layer caching
COPY package*.json ./

# Install dependencies
RUN npm install

COPY ./public ./public
COPY ./src ./src
COPY ./tsconfig.json ./

# Expose the port the app runs on
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
