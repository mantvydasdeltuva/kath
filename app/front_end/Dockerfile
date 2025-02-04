FROM node:latest

# Expose frontend port and set frontend files directory.
EXPOSE 5173
ARG APP_DIR="/kath/front_end"

# Copy package.json file to the image and install the dependencies to the root directory so replacing the frontend directory via mounting doesn't hide them later.
WORKDIR /
COPY ./package.json .
RUN npm install

# Copy frontend files to the imag
WORKDIR ${APP_DIR}
COPY . .

ENTRYPOINT []
CMD ["/bin/bash", "-c", "npm run dev"]
