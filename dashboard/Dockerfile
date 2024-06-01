# Use an official Node runtime as a parent image
FROM node:14-alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 3000
EXPOSE 3000

# Start the React app in development mode
CMD ["npm", "start"]

##### PROD MODE #####

# # Build the app
# RUN npm run build

# # Use an official Nginx image to serve the React application
# FROM nginx:alpine

# # Copy the build output to the Nginx html directory
# COPY --from=0 /app/build /usr/share/nginx/html

# # Start Nginx
# CMD ["nginx", "-g", "daemon off;"]

